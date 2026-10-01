from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate,login,logout

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",

                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes=[]
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return Response(
                {
                    "error": "Invalid credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        login(request, user)
        return Response(
            {
                "message": "Credentials verified",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            },
            status=status.HTTP_200_OK
        )

class ProfileView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        return Response({
            "messsage":"authenticated sucessfully",
            "user":{
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            }
        })
class SessionProfileView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "message": "Authenticated using session",
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            }
        })
        
class LogoutView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        logout(request)

        return Response({
            "message": "Logout successful"
        })
class TokenProfileView(APIView):

    authentication_classes = [
        TokenAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        return Response({
            "message": "Authenticated using token",
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            },
            "token": str(request.auth)
        })
class TokenLogoutView(APIView):

    authentication_classes = [
        TokenAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        request.auth.delete()

        return Response({
            "message": "Token invalidated"
        })

class JWTProfileView(APIView):

    authentication_classes = [
        JWTAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        return Response({
            "message": "Authenticated using JWT",
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            }
        })