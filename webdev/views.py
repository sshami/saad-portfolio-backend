from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Webdev
from .serializers import WebdevSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class WebdevPageView(APIView):
    # Using either token authentication for client-server (frontend client app / backend service app) auth
    # or JWT authentication for app user (for future use in case it is needed)
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        webdev_page = Webdev.objects.all()
        serializer = WebdevSerializer(webdev_page, many=True)
        return Response(serializer.data)