from django.shortcuts import render
from .models import Role
from django.http import JsonResponse
import json 
# Create your views here.
def create_role(request):
    if request.method=='POST':
        data = json.loads(request.body)
        access_modules = data.get('accessModules')
        if not isinstance(data.get('roleName'),str) or not data.get('roleName').strip():
            return JsonResponse({
                'success':False,
                "message":"roleName is required"
            },status=400)
        if (
            access_modules is None
            or not isinstance(access_modules,list)
            or not all(isinstance(module,str) for module in access_modules)
        ):
            return JsonResponse({
                "success":False,
                "message":"access modules are required and shpuld be a list of strings"
            })
            
        role = Role.objects.create(
            roleName=data.get('roleName'),
            accessModules=data.get('accessModules')
        )
        return JsonResponse({
            "success": True,
            "message": "Role created successfully",
            "role": {
                "id": role.id,
                "roleName": role.roleName,
                "accessModules": role.accessModules,
                "active": role.active,
                "created_at": role.created_at.isoformat(),
            }
        }, status=201)
    return JsonResponse({
        "success":False,
        "message":"error creating the role"
    },status = 405)

def get_all_roles(request):
    return None