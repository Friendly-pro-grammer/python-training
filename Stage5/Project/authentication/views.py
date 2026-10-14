import requests
from rest_framework.views import APIView
from rest_framework import status
from .serialzers import RegisterSerializer,ProfileSerializer,GoogleSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings


class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message":"User registerd successfully",
                    "user":{
                        "id":user.id,
                        "name":user.name,
                        "email":user.email
                    }
                },status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ProfileView(APIView):
    permission_classes =[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]
    
    def get(self, request):
        serializer = ProfileSerializer(request.user)

        return Response(serializer.data)
    def patch(self,request):
        serializer = ProfileSerializer(
            request.user,
            data = request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                {
                    "message":"Profile updated successfully",
                    "user":serializer.data
                },status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=400
        )


# # class GoogleLoginView(APIView):
#     authentication_classes = []
#     permission_classes = []
#     def post(self, request):
#         serializer = GoogleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if not settings.GOOGLE_CLIENT_ID:
#             return Response(
#                 {"error": "Google Client ID is not configured on the server"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
#         try:
#             # Verifies signature, issuer, expiry, and audience (GOOGLE_CLIENT_ID)
#             info = google_id_token.verify_oauth2_token(
#                 serializer.validated_data["id_token"],
#                 google_requests.Request(),
#                 settings.GOOGLE_CLIENT_ID,
#             )
#         except ValueError:
#             return Response(
#                 {"error": "Invalid or expired Google token"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         if not info.get("email_verified"):
#             return Response(
#                 {"error": "Google email is not verified"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         sub = info.get("sub")
#         email = info.get("email", "").lower()
#         name = (
#             info.get("name")
#             or f"{info.get('given_name', '')} {info.get('family_name', '')}".strip()
#             or "Google User"
#         )
#         with transaction.atomic():
#             user = User.objects.filter(google_sub=sub).first()
#             created = False
#             if user is None:
#                 # Check for existing email/password user to link accounts
#                 user = User.objects.filter(email=email).first()
#                 if user:
#                     user.google_sub = sub
#                     # Update name if previously blank
#                     if not user.name:
#                         user.name = name
#                     user.save(update_fields=["google_sub", "name"])
#                 else:
#                     # Use create_user to properly handle password hashing / unusable password
#                     user = User.objects.create_user(
#                         email=email,
#                         name=name,
#                         password=None,  # Automatically marks password as unusable
#                         google_sub=sub,
#                         is_active=True,
#                     )
#                     created = True
#         if not user.is_active:
#             return Response(
#                 {"error": "Account disabled"},
#                 status=status.HTTP_403_FORBIDDEN,
#             )
#         # Generate SimpleJWT tokens
#         refresh = RefreshToken.for_user(user)
#         return Response(
#             {
#                 "tokens": {
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                 },
#                 "user": {
#                     "id": user.id,
#                     "email": user.email,
#                     "name": user.name,
#                 },
#                 "is_new_user": created,
#             },
#             status=status.HTTP_200_OK,
#         )        