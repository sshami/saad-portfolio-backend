from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Photography, PhotographyAlbum
from .serializers import PhotographySerializer, PhotographyAlbumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class PhotographyPageView(APIView):
    # Using either token authentication for client-server (frontend client app / backend service app) auth
    # or JWT authentication for app user (for future use in case it is needed)
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        photography_page = Photography.objects.all()
        serializer = PhotographySerializer(photography_page, many=True)
        return Response(serializer.data)

class PhotographyAlbumsView(APIView):
    # Using either token authentication for client-server (frontend client app / backend service app) auth
    # or JWT authentication for app user (for future use in case it is needed)
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        albums = PhotographyAlbum.objects.filter(live=True)
        album_slug = request.query_params.get('album', None)
        if album_slug is not None:
            albums = PhotographyAlbum.objects.filter(slug=album_slug)
        serializer = PhotographyAlbumSerializer(albums, many=True, context={"request": request})
        return Response(serializer.data)

