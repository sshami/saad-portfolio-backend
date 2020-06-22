from django.conf import settings
from .models import Photography, PhotographyAlbum
from rest_framework import serializers

class PhotographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photography
        fields = ['id', 'title', 'slug', 'page_description' , 'default_album']
        depth = 1


class PhotographyAlbumSerializer(serializers.ModelSerializer):

    photos = serializers.SerializerMethodField()

    class Meta:
        model = PhotographyAlbum
        fields = ['id', 'title', 'slug', 'url_path', 'photos', 'title_font_size']
        depth = 1

    # Need to unpack the image block field
    # in order to include image file URL to serialized model
    def get_photos(self, obj):
        album_photos = []
        for block in obj.photos:
            photo_id = block.id
            value = {
                'title': block.value.get('title'),
                'image_url': settings.HOSTNAME + block.value.get('image').file.url,
                'credit_one': block.value.get('credit_one'),
                'credit_two': block.value.get('credit_two'),
                'credit_three': block.value.get('credit_three'),
                'credit_four': block.value.get('credit_four'),
            }
            album_photos.append({'id': photo_id, 'value': value})
        return album_photos

