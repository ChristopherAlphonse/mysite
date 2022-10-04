from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from wagtail.core import blocks




class GenericPage(Page):
   banner_title = models.CharField(
   max_length=255, 
   default="Welcome to Generic")
   
   introduction = models.TextField(help_text="Text to describe the page", blank=True)
   banner_image = models.ForeignKey(
      "wagtailimages.Image",
      null=True,
      blank=False,
      on_delete=models.SET_NULL,
      related_name="+",
      help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
   )
   
   author = models.ForeignKey(
      "Author",
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name="+"
   )
   
   body = StreamField([
      ('heading', blocks.CharBlock()),
      ('paragraph',blocks.RichTextBlock()),
      ('image', ImageChooserBlock()),
], null=True,
   block_counts={
   'heading': {'min_num': 1},
   'image': {'max_num': 5},
}, use_json_field=True)

   content_panels = Page.content_panels + [
      FieldPanel('banner_title'),
      FieldPanel("introduction"),
      FieldPanel("banner_image"),
      SnippetChooserPanel("author"),
      FieldPanel("body")
]

@register_snippet
class Author(models.Model):
   name = models.CharField(max_length=100) 
   title = models.CharField(blank=True, max_length=100)
   company_name = models.CharField( blank=True, max_length=100)
   company_url = models.URLField(blank=True)
   image = models.ForeignKey(
      "wagtailimages.Image",
      null=True,
      blank=False,
      on_delete=models.SET_NULL,
      related_name="+"
   )
   
   panels = [
      FieldPanel("name"),
      FieldPanel("title"),
      FieldPanel("company_name"),
      FieldPanel("company_url"),
      FieldPanel("image")
   ]
   def __str__(self):
      return self.name 