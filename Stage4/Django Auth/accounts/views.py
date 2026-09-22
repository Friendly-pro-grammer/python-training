from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
# Create your views here.
import json
from django.contrib.auth import authenticate, login ,logout
from django.views.decorators.csrf import ensure_csrf_cookie

User = get_user_model()

def register(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=405
        )
    data = json.loads(request.body)
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get("role","EMPLOYEE")
    if not username or not password:
        return JsonResponse(
            {"error": "Username and password are required"},
            status=400
        )
    if User.objects.filter(username=username).exists():
        return JsonResponse(
            {"error": "Username already exists"},
            status=400
        )
    user = User.objects.create(
        username=username,
        email=email,
        password=password,
        role=role
    )
    return JsonResponse({
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "username": user.username,
        }},status=201)


def login_user(request):
    if request.method!="POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=405
        )
    data= json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    
    user = authenticate(username=username,password=password)
    if user is None:
        return JsonResponse(
            {"error": "Invalid username or password"},
            status=401
        )
    login(request,user)
    return JsonResponse({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    })
    
def logout_user(request):

    logout(request)

    return JsonResponse({
        "message": "Logout successful"
    })

def profile(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"error": "Authentication required"},
            status=401
        )
    return JsonResponse({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
        "role": request.user.role
    })

def protected_endpoint(request):

    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "error": "You must be logged in"
            },
            status=401
        )

    return JsonResponse({
        "message": "You successfully accessed the protected endpoint!",
        "user": request.user.username
    })
@ensure_csrf_cookie
def csrf_token(request):
    return JsonResponse({
        "message": "CSRF cookie set"
    })