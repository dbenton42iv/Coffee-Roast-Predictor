from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UploadView(APIView):
    def post(self, request, *args, **kwargs):
        # Your upload logic here
        return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)

class PredictView(APIView):
    def post(self, request, *args, **kwargs):
        # Your prediction logic here
        return Response({'prediction': 'result'}, status=status.HTTP_200_OK)

class RetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        # Your retrieve logic here
        return Response({'data': 'your retrieved data'}, status=status.HTTP_200_OK)