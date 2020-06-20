from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class Photography(Page):
    page_description = models.CharField(max_length=255)
    default_album = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
        PageChooserPanel('default_album', 'photography.PhotographyAlbum'),
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


class PhotographyAlbum(Page):
    title_font_size = models.DecimalField('Title Font Size', max_digits=5, decimal_places=2, default=12.5)
    photos = StreamField([
        ('Image', ImageCaptionBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('title_font_size'),
        StreamFieldPanel('photos'),
    ]

    parent_page_type = [
        'photography.Photography'
    ]




