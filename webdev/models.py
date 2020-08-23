from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import PageChooserBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import PageChooserPanel


# Web Development Homepage
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


# Web Project item (used for StreamField)
class WebProject(blocks.StructBlock):
    demo_laptop_display = ImageChooserBlock(required=True)
    demo_mobile_display = ImageChooserBlock(required=False)

    class Meta:
        icon = 'image'


# Standard Project item (used for StreamField)
class StandardProject(blocks.StructBlock):
    demo_display = ImageChooserBlock(required=True)

    class Meta:
        icon = 'image'


# Web Development Project Listing
class WebdevProject(Page):
    summary = models.TextField()
    display_image = StreamField(
        StreamBlock([
            ('WebProject', WebProject()),
            ('StandardProject', StandardProject())
        ], min_num=0, max_num=1)
    )
    web_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        StreamFieldPanel('display_image'),
        FieldPanel('web_url')
    ]

    parent_page_type = [
        'webdev.Webdev'
    ]


# Single Image with Caption
class SingleImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.TextBlock(required=False)

    class Meta:
        icon = 'image'


# Double Image with Caption
class DoubleImageBlock(blocks.StructBlock):
    image_left = ImageChooserBlock(required=True)
    image_right = ImageChooserBlock(required=True)
    caption = blocks.TextBlock(required=False)

    class Meta:
        icon = 'image'


# Project Detail Page
class ProjectDetailPage(Page):
    project_listing = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('single_image', SingleImageBlock()),
        ('double_image', DoubleImageBlock())
    ])

    content_panels = Page.content_panels + [
        PageChooserPanel('project_listing', 'webdev.WebdevProject'),
        StreamFieldPanel('body')
    ]
