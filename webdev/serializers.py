from rest_framework import serializers
from .models import Webdev, WebdevProject, ProjectDetailPage
from django.conf import settings
from rest_framework.generics import get_object_or_404


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


class ProjectDetailPageSerializer(serializers.ModelSerializer):

    body = serializers.SerializerMethodField()
    project_listing = serializers.SerializerMethodField()

    class Meta:
        model = ProjectDetailPage
        fields = ['id', 'title', 'slug', 'project_listing', 'body']
        depth = 1

    # Need to unpack the page chooser block field
    # in order to display all needed contents for project detail page listing
    # TODO: Make this more DRY - consider merging the WebDevProject and ProjectDetailPage models
    def get_project_listing(self, obj):
        project_listing_page = {}
        project_listing_page['images'] = {}
        project_listing_id = obj.project_listing.id
        project_listing_obj = get_object_or_404(WebdevProject, id=project_listing_id)
        project_display_image_type = project_listing_obj.display_image.stream_data[0].get('type')
        project_listing_page['type'] = project_display_image_type
        project_listing_demo_web_url = project_listing_obj.web_url
        project_listing_page['url'] = project_listing_demo_web_url
        if project_display_image_type == 'WebProject':
            project_listing_page['images']['demo_laptop_display'] = \
                settings.HOSTNAME + \
                project_listing_obj.display_image[0].value.get('demo_laptop_display').file.url
            project_listing_page['images']['demo_mobile_display'] = \
                settings.HOSTNAME + \
                project_listing_obj.display_image[0].value.get('demo_mobile_display').file.url
            project_listing_page['images']['demo_laptop_display-mobile'] = \
                settings.HOSTNAME + \
                project_listing_obj.display_image[0].value.get('demo_laptop_display').get_rendition('width-700').url
            project_listing_page['images']['demo_mobile_display-mobile'] = \
                settings.HOSTNAME + \
                project_listing_obj.display_image[0].value.get('demo_mobile_display').get_rendition('width-700').url
        elif project_display_image_type == 'StandardProject':
            project_listing_page['images']['demo_display'] = \
                settings.HOSTNAME + \
                project_listing_obj.display_image[0].value.get('demo_display').file.url
            project_listing_page['images']['demo_display-mobile'] = \
                settings.HOSTNAME + \
                project_listing_obj.display_image[0].value.get('demo_display').get_rendition('width-700').url

        return project_listing_page


    # Need to unpack the body streamfield
    # in order to display all needed content for project detail page body
    def get_body(self, obj):
        body_items = []
        for block in obj.body:
            item = {}
            item['type'] = block.block.name
            body_items.append(item)
            if item['type'] == 'single_image':
                item['image'] = settings.HOSTNAME + block.value.get('image').file.url
                item['image-mobile'] = settings.HOSTNAME + block.value.get('image').get_rendition('width-700').url
            elif item['type'] == 'double_image':
                item['image_left'] = settings.HOSTNAME + block.value.get('image_left').file.url
                item['image_right'] = settings.HOSTNAME + block.value.get('image_right').file.url
                item['image_left-mobile'] = settings.HOSTNAME + \
                    block.value.get('image_left').get_rendition('width-700').url
                item['image_right-mobile'] = settings.HOSTNAME + \
                    block.value.get('image_right').get_rendition('width-700').url
            elif item['type'] == 'paragraph':
                # TODO: Sanitize HTML (if not already done by Wagtail) to protect from XSS
                item['content'] = block.value.source

        return body_items

