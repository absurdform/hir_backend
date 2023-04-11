from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

# from wagtail.images.blocks import ImageChooserBlock
from .blocks import CardBlock

class HomePage(Page):
    '''Home Page Model'''

    templates = 'home/home_page.html'
    max_count = 1

    banner_title = models.CharField(max_length=255, blank=False, null=True)
    banner_subtitle = RichTextField(blank=True)

    platforms = StreamField([
        ('epr_component', blocks.ListBlock(CardBlock(), icon = 'globe')),
    ], use_json_field=True, null=True, blank=True, min_num = 1, max_num = 1)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("platforms"),
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class DetailsPage(Page):
    '''Details page'''

    templates = 'home/details_page.html'

    content_list = StreamField([
        ('content', blocks.ListBlock(CardBlock(), icon='clipboard-list')),
    ], use_json_field=True, null=True, blank=True, min_num = 1, max_num = 1)

    content_panels = Page.content_panels + [
        FieldPanel("content_list"),
    ]

