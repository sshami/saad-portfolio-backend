from rest_framework import serializers
from .models import Webdev, WebdevProject
from django.conf import settings

class WebdevSerializer(serializers.ModelSerializer):

    featured_projects = serializers.SerializerMethodField()

    class Meta:
        model = Webdev
        fields = ['id', 'title', 'slug', 'page_description', 'featured_projects']
        depth = 1

    # Need to unpack the page chooser block field
    # in order to display all needed contents for featured projects
    def get_featured_projects(self, obj):
        feat_projects = []
        for block in obj.featured_projects:
            project_id = block.id

            # Get display images for the project depending on the type of project (WebProject or StandardProject)
            # WebProjects have two images (laptop demo display and mobile demo display)
            # StandardProject has only one image
            display_images = {}
            display_image_type = block.value.display_image.stream_data[0].get('type')
            display_images['type'] = display_image_type
            display_images['images'] = {}

            if display_image_type == 'WebProject':
                display_images['images']['demo_laptop_display'] = \
                    settings.HOSTNAME + \
                    block.value.display_image[0].value.get('demo_laptop_display').file.url
                display_images['images']['demo_mobile_display'] = \
                    settings.HOSTNAME + \
                    block.value.display_image[0].value.get('demo_mobile_display').file.url
                display_images['images']['demo_laptop_display-mobile'] = \
                    settings.HOSTNAME + \
                    block.value.display_image[0].value.get('demo_laptop_display').get_rendition('width-700').url
                display_images['images']['demo_mobile_display-mobile'] = \
                    settings.HOSTNAME + \
                    block.value.display_image[0].value.get('demo_mobile_display').get_rendition('width-700').url

            elif display_image_type == 'StandardProject':
                display_images['images']['demo_display'] = \
                    settings.HOSTNAME + \
                    block.value.display_image[0].value.get('demo_display').file.url
                display_images['images']['demo_display-mobile'] = \
                    settings.HOSTNAME + \
                    block.value.display_image[0].value.get('demo_display').get_rendition('width-700').url


            # Gather all values for this featured project
            value = {
                'title': block.value.title,
                'slug': block.value.slug,
                'web_url': block.value.web_url,
                'summary': block.value.summary,
                'display_image': display_images
            }

            feat_projects.append({'id': project_id, 'value': value})

        return feat_projects