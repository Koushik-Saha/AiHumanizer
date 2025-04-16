from celery.result import AsyncResult
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HumanizeTextSerializer
from .tasks import humanize_text_task
from django.http import FileResponse, Http404
from .models import Submission
from .export_utils import generate_docx, generate_pdf
from .serializers import SentenceEditorSerializer
from .editor import sentence_editor

class HumanizeTextView(APIView):
    def post(self, request, format=None):
        serializer = HumanizeTextSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            detection_evasion = serializer.validated_data['detection_evasion']
            plagiarism_check = serializer.validated_data['plagiarism_check']
            task = humanize_text_task.delay(content, detection_evasion, plagiarism_check)
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

class ExportSubmissionView(APIView):
    """
    Export a past submission as PDF or DOCX.
    """
    authentication_classes = [APIKeyAuthentication]
    throttle_classes = [APIKeyThrottle]

    def get(self, request, submission_id):
        fmt = request.query_params.get('format', 'pdf').lower()
        try:
            submission = Submission.objects.get(id=submission_id)
        except Submission.DoesNotExist:
            raise Http404("Submission not found")

        if fmt == 'pdf':
            buf = generate_pdf(submission)
            return FileResponse(buf, as_attachment=True, filename=f"submission_{submission_id}.pdf")
        elif fmt == 'docx':
            buf = generate_docx(submission)
            return FileResponse(buf, as_attachment=True, filename=f"submission_{submission_id}.docx")
        else:
            return Response({"error": "Invalid format"}, status=400)

class SentenceEditorView(APIView):
    """
    Return humanized versions of each sentence for editing.
    """
    def post(self, request, format=None):
        serializer = SentenceEditorSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            detection_evasion = serializer.validated_data['detection_evasion']
            result = sentence_editor(content, detection_evasion)
            return Response({"sentences": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

