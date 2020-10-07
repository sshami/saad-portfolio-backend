from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Homepage, About
from .serializers import HomepageSerializer, AboutSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class HomepageView(APIView):
    # Using either token authentication for client-server (frontend client app / backend service app) auth
    # or JWT authentication for app user (for future use in case it is needed)
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        homepage = Homepage.objects.all()[:1]
        serializer = HomepageSerializer(homepage, many=True)
        return Response(serializer.data)


class AboutView(APIView):
    # Using either token authentication for client-server (frontend client app / backend service app) auth
    # or JWT authentication for app user (for future use in case it is needed)
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        about_page = About.objects.all()[:1]
        serializer = AboutSerializer(about_page, many=True)
        return Response(serializer.data)

