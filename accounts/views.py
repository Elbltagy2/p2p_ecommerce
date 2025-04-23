# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer

# Registration view
class RegisterView(APIView):
    def post(self, request):
        # Instantiate the serializer with the data from the request
        serializer = UserSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            serializer.save()  # Create and save the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the user data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Login view to authenticate user and issue JWT tokens
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
