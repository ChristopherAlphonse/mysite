from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    banner_title = models.CharField(
        max_length=255, default="Welcome to the Home Page")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('banner_title')

    ]
