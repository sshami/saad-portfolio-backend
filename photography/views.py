from rest_framework import viewsets
from .models import Photography
from .serializers import PhotographySerializer


class PhotographyViewSet(viewsets.ModelViewSet):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer