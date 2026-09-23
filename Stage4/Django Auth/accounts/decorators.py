from functools import wraps
from django.http import JsonResponse


def role_required(*allowed_roles):
    def decorator(view_function):
        @wraps(view_function)
        def wrapper(request,*args,**kwargs):
            if not request.user.is_authenticated:
                return JsonResponse(
                    {
                        "error": "Authentication required"
                    },
                    status=401
                )
            if request.user.role not in allowed_roles:
                return JsonResponse(
                    {
                        "error": "You don't have permission"
                    },
                    status=403
                )
            return view_function(
                request,
                *args,
                **kwargs
            )
        return wrapper
    return decorator
        