from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.api import APIField


class Homepage(Page):
    bio_title = models.CharField(max_length=255)
    bio_paragraph1 = models.CharField(max_length=255)
    bio_paragraph2 = models.CharField(max_length=255)
    contact_email = models.EmailField('Email', blank=False)
    contact_instagram = models.URLField('Instagram', blank=True)
    contact_facebook = models.URLField('Facebook', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('bio_title'),
        FieldPanel('bio_paragraph1'),
        FieldPanel('bio_paragraph2'),
        FieldPanel('contact_email'),
        FieldPanel('contact_instagram'),
        FieldPanel('contact_facebook')
    ]