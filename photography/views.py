from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Photography, PhotographyAlbum
from .serializers import PhotographySerializer, PhotographyAlbumSerializer
from rest_framework.permissions import IsAuthenticated


class PhotographyPageView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        photography_page = Photography.objects.all()
        serializer = PhotographySerializer(photography_page, many=True)
        return Response(serializer.data)

class PhotographyAlbumsView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        albums = PhotographyAlbum.objects.filter(live=True)
        album_slug = request.query_params.get('album', None)
        if album_slug is not None:
            albums = PhotographyAlbum.objects.filter(slug=album_slug)
        serializer = PhotographyAlbumSerializer(albums, many=True)
        return Response(serializer.data)

