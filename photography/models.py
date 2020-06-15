from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from pprint import pprint

from wagtail.api import APIField

class Photography(Page):
    page_description = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
    ]

    subpage_types = [
        'photography.PhotographyAlbum',
    ]


class ImageCaptionBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=False)
    credit_one = blocks.CharBlock(required=False)
    credit_two = blocks.CharBlock(required=False)
    credit_three = blocks.CharBlock(required=False)
    credit_four = blocks.CharBlock(required=False)

    class Meta:
        icon = 'image'

    def get_api_representation(self, value, context=None):
        if (value):
            """ Recursively call get_api_representation on children and return as a plain dict """
            #print(value["title"]);
            #pprint(vars(value["image"]))
            dict = {
                'title': value['title'],
                'image_url': value["image"].file.url,
                'credit_one': value['credit_one'],
                'credit_two': value['credit_two'],
                'credit_three': value['credit_three'],
                'credit_four': value['credit_four'],
            }
        else:
            dict = {}

        return dict


class PhotographyAlbum(Page):
    photos = StreamField([
        ('Image', ImageCaptionBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('photos'),
    ]

    api_fields = [
        APIField('photos'),
    ]

    parent_page_type = [
        'photography.Photography'
    ]




