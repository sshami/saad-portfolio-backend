from .models import Homepage
from rest_framework import serializers


class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = ['id', 'title', 'slug', 'bio_title', 'bio_paragraph1', 'bio_paragraph2', 'contact_email',
                  'contact_instagram', 'contact_facebook']
        depth = 1
