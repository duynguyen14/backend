from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

class HomePage(APIView):
    # def get(self, request):
    #     data = {
    #         "title": "Welcome to My Home Page",
    #         "description": "This is the home page of my application."
    #     }
    #     return Response(data)
    def get(self, request):
        # Lấy tất cả người dùng
        users = User.objects.all()
        # Serialize dữ liệu người dùng
        user_serializer = UserSerializer(users, many=True)
        # Trả về danh sách người dùng dưới dạng JSON
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdateUserView(APIView):
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                serializer=UserSerializer(user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)  # Lấy access token
                refresh_token = str(refresh)  # Lấy refresh token
                print(f"Access Token: {access_token}")
                return Response(
                    {
                    "message": "Login successful!",
                    "user":serializer.data,
                    "access_token": access_token,
                    "refresh_token": refresh_token
                    }, 
                    status=status.HTTP_200_OK
                    )
            else:
                return Response({"error": "Invalid email or password."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_400_BAD_REQUEST)