from rest_framework.views import APIView
from .serializers import RegisterSerializers
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
            )
