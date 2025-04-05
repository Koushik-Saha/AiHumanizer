from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HumanizeTextSerializer

class HumanizeTextView(APIView):
    def post(self, request, format=None):
        serializer = HumanizeTextSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            # Dummy humanization logic: prefix the content
            humanized_content = f"Humanized: {content}"
            return Response({"humanized_content": humanized_content}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)