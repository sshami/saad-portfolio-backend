from django.conf import settings
from .models import Homepage, About
from rest_framework import serializers


class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = ['id', 'title', 'slug', 'bio_title', 'bio_paragraph1', 'bio_paragraph2', 'contact_email',
                  'contact_instagram', 'contact_facebook']
        depth = 1


class AboutSerializer(serializers.ModelSerializer):

    bio_image = serializers.SerializerMethodField()

    homepage = Homepage.objects.all()[0]
    instagram = homepage.contact_instagram
    email = homepage.contact_email
    facebook = homepage.contact_facebook
    contact_email = serializers.CharField(default=email)
    contact_instagram = serializers.CharField(default=instagram)
    contact_facebook = serializers.CharField(default=facebook)

    class Meta:
        model = About
        fields = ['bio_image', 'body', 'contact_email', 'contact_instagram', 'contact_facebook']
        depth = 1

    def get_bio_image(self, obj):
        return settings.HOSTNAME + obj.bio_image.file.url
