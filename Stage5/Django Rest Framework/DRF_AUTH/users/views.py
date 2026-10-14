from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,UploadedFileSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate,login,logout
from .decorators import log_api_access,require_staff
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from django.core.cache import cache
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import UploadFile
from django.http import FileResponse
from django.core.exceptions import SuspiciousFileOperation


User = get_user_model()

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
    @log_api_access
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
        
        
class staffDashBoard(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    @require_staff
    def get(self, request):

        return Response({
            "message": "Welcome to the staff dashboard.",
            "user": request.user.username,
            "is_staff": request.user.is_staff
        })


class UserCountView(APIView):
    
    def get(self,request):
        cache_key = "users:count"
        user_count = cache.get(cache_key)
        if user_count is None:
            user_count = User.objects.count()
            cache.set(cache_key, user_count, timeout=60)
        return Response({
            "total_users": user_count
        })
        
class FileUploadView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    parser_classes=[MultiPartParser,FormParser]
    
    def post(self,request):
        serializer =UploadedFileSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        uploaded_file = serializer.save()
        return Response({
            "message":"file upload successfull",
            "file":{
                "id":uploaded_file.id,
                "name":uploaded_file.original_name,
                "uploaded_at":uploaded_file.uploaded_at,
            }
        },status=status.HTTP_201_CREATED)

def get_user_file_or_404(request,file_id):
    return get_object_or_404(
        UploadFile,
        id=file_id,
        owner=request.user,
    )


class FileListView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        files=UploadFile.objects.filter(owner = request.user).order_by("-uploaded_at")
        data = [
            {
                "id": item.id,
                "name": item.original_name,
                "uploaded_at": item.uploaded_at,
            }
            for item in files
        ]
        return Response({"files": data})

class FileDownloadView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request,file_id):
        uploaded_file = get_user_file_or_404(
            request,file_id
        )
        return FileResponse(
            uploaded_file.file.open("rb"),
            as_attachment=True,
            filename=uploaded_file.original_name,
        )       