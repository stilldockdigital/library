from wagtail.models import Page
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import  RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    pass

class LandingPage(Page):
    
    heading = models.CharField(max_length = 250, null=True)
    intro = RichTextField(null=True)
    
    content_panels = Page.content_panels + [  
        FieldPanel('heading'),
        FieldPanel('intro'),
       

    ]

class ArticlePage(Page):   
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    heading = models.CharField(max_length = 250, null=True)
    intro = RichTextField(null=True)
    paragraph = RichTextField(null=True)
    image = models.ForeignKey(
            'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
        )
    category = models.ForeignKey(
            'home.ArticleCategory', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
        ) 

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('paragraph'),
        FieldPanel('image'),
        FieldPanel('category'),

    ]

    
@register_snippet
class ArticleCategory(models.Model):
    category = models.CharField(max_length = 250, null=True)
    description = RichTextField(null=True)
    
    panels = [
        
        FieldPanel('category'),
        FieldPanel('description'),   
       
    ]

    def __str__(self):
            return self.category
