import logging
import time
from functools import wraps
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger("django")


def log_api_access(view_func):
    @wraps(view_func)
    def wrapper(self,request,*args,**kwargs):
        start_time = time.perf_counter()
        response = view_func(
            self, request, *args, **kwargs
        )
        duration = (time.perf_counter() - start_time) * 1000
        user_id = (
            request.user.id
            if request.user.is_authenticated
            else "anonymous"
        )
        logger.info(
            "View=%s Method=%s Path=%s User=%s Status=%s Duration=%.2fms",
            view_func.__name__,
            request.method,
            request.path,
            user_id,
            response.status_code,
            duration,
        )
        return response
    return wrapper


def require_staff(view_func):
    @wraps(view_func)
    def wrapper(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return Response({
                "Message":"Authentication is required",
                
            },status=status.HTTP_401_UNAUTHORIZED)
        if not request.user.is_staff:
            return Response(
                {"detail": "Staff access required."},
                status=status.HTTP_403_FORBIDDEN
            )
        return view_func(self, request, *args, **kwargs)
    return wrapper