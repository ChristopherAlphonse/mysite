from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class GenericPage(Page):
   banner_title = models.CharField(
   max_length=255, 
   default="Welcome to Generic")

   content_panels = Page.content_panels + [
      FieldPanel('banner_title')
]
