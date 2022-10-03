from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel



class GenericPage(Page):
   banner_title = models.CharField(
   max_length=255, 
   default="Welcome to Generic")
   
   introduction = models.TextField(blank=True)
   banner_image = models.ForeignKey(
      "wagtailimages.Image",
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name="+"
   )

   content_panels = Page.content_panels + [
      FieldPanel('banner_title'),
      FieldPanel("introduction"),
      FieldPanel("banner_image"),
]
