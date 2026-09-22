from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
# Create your views here.
from .forms import StudentForm
from .models import Student

def student_create(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return JsonResponse({
                "success":True,
                "message":"form saved successfully",
                "data":{
                    "id":student.id,
                    "name":student.name,
                    "age":student.age,
                    "email":student.email
                    
                }
            })
        return JsonResponse({
                    "success": False,
                    "errors": form.errors,
                }, status=400)
    return JsonResponse({
            "success": False,
            "errors": form.errors,
        }, status=400)
    
def student_list(request):
    student  = Student.objects.all()
    return JsonResponse({
        "success": True,
        "data": list(student.values())
    })
def student_detail(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return JsonResponse({
        "success": True,
        "data": {
            "id": student.id,
            "name": student.name,
            "email": student.email,
        }
    })

    
def student_edit(request,pk):
    if request.method =='POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                student = form.save()
                return JsonResponse({
                    "success": True,
                    "message": "Student updated successfully",
                    "data": {
                        "id": student.id,
                        "name": student.name,
                        "email": student.email,
                    }
                })
            return JsonResponse({
                                "success": False,
                                "errors": form.errors,
                            }, status=400)
    return JsonResponse({
            "success": False,
            "errors": form.errors,
        }, status=400)  
    
def student_delete(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.delete()
        return JsonResponse({
            "success":True,
            "message":"User deleted successfully "
        })
    return JsonResponse({
        "success": False,
        "message": "Only POST requests are allowed",
    }, status=405)