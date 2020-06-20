from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Homepage
from .serializers import HomepageSerializer

class HomepageView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        photography_page = Homepage.objects.all()
        serializer = HomepageSerializer(photography_page, many=True)
        return Response(serializer.data)

