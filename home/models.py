from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    event = models.CharField(max_length=250, blank=True)
    about = RichTextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    literal_date = models.CharField(max_length=250, blank=True)
    url_get_tickets = models.URLField(blank=True)
    event_date = models.DateField(blank=True, null=True)

    logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )



    content_panels = Page.content_panels + [
        FieldPanel('event'),
        FieldPanel('about'),
        FieldPanel('location'),
        FieldPanel('literal_date'),
        FieldPanel('url_get_tickets'),
        FieldPanel('event_date'),
        FieldPanel('logo_image'),
        FieldPanel('hero_image'),
    ]


# TODO create class for next segment