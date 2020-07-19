from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import PageChooserBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class Webdev(Page):
    page_description = models.CharField(max_length=255)
    featured_projects = StreamField([
        ('Project', PageChooserBlock(page_type='webdev.WebdevProject'))
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
        StreamFieldPanel('featured_projects')
    ]

    subpage_types = [
        'webdev.WebdevProject',
    ]


class WebProject(blocks.StructBlock):
    demo_laptop_display = ImageChooserBlock(required=True)
    demo_mobile_display = ImageChooserBlock(required=False)

    class Meta:
        icon = 'image'


class StandardProject(blocks.StructBlock):
    demo_display = ImageChooserBlock(required=True)

    class Meta:
        icon = 'image'


class WebdevProject(Page):
    summary = models.TextField()
    display_image = StreamField(
        StreamBlock([
            ('WebProject', WebProject()),
            ('StandardProject', StandardProject())
        ], min_num=0, max_num=1)
    )

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        StreamFieldPanel('display_image'),
    ]

    parent_page_type = [
        'webdev.Webdev'
    ]
