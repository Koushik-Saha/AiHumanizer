from celery.result import AsyncResult
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HumanizeTextSerializer
from .tasks import humanize_text_task

class HumanizeTextView(APIView):
    def post(self, request, format=None):
        serializer = HumanizeTextSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            task = humanize_text_task.delay(content)
            return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusView(APIView):
    def get(self, request, task_id, format=None):
        task_result = AsyncResult(task_id)
        if task_result.state == 'PENDING':
            response = {'state': task_result.state, 'status': 'Pending...'}
        elif task_result.state != 'FAILURE':
            response = {'state': task_result.state, 'result': task_result.result}
        else:
            response = {'state': task_result.state, 'status': str(task_result.info)}
        return Response(response)