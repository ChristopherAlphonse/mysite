
from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel




class GenericPage(Page):
   banner_title = models.CharField(
   max_length=255, 
   default="Welcome to Generic")
   
   introduction = models.TextField(blank=True)
   banner_image = models.ForeignKey(
      "wagtailimages.Image",
      null=True,
      blank=False,
      on_delete=models.SET_NULL,
      related_name="+"
   )
   
   author = models.ForeignKey(
      "Author",
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name="+"
   )

   content_panels = Page.content_panels + [
      FieldPanel('banner_title'),
      FieldPanel("introduction"),
      FieldPanel("banner_image"),
      SnippetChooserPanel("author")
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