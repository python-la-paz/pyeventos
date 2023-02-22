from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    event = models.CharField(max_length=250, blank=True)
    about = RichTextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    literal_date = models.CharField(max_length=250, blank=True)
    url_get_tickets = models.URLField(blank=True)
    text_get_tickets = models.CharField(max_length=250, blank=True, default="Get tickets")
    event_date = models.DateField(blank=True, null=True)

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("event"),
        FieldPanel("about"),
        FieldPanel("location"),
        FieldPanel("literal_date"),
        FieldPanel("url_get_tickets"),
        FieldPanel("text_get_tickets"),
        FieldPanel("event_date"),
        FieldPanel("logo_image"),
        FieldPanel("hero_image"),
    ]
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        segments = SegmentPage.objects.child_of(self).live().order_by("order")
        context["segments"] = segments #sorted (segments, key=lambda x: x.order)
        return context

class InformationBlock(blocks.StructBlock):
            lni_icon = blocks.CharBlock(help_text = "(lni lni-help) https://lineicons.com/icons/")
            title = blocks.CharBlock()
            description = blocks.CharBlock()

class SegmentPage(Page):
    order = models.IntegerField(default=0)
    segments = StreamField(
        [
        # detail segment
            (
                "detail_segment",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock(max_length=250, blank=False)),
                        ("description", blocks.RichTextBlock(required=False)),
                        ("list_options", blocks.ListBlock(blocks.CharBlock(required=False))),
                        ("url", blocks.URLBlock(required=False)),
                        ("url_text", blocks.CharBlock(max_length=250, required=False, default="More info")),
                        ("image", ImageChooserBlock(required=False)),
                        (
                            "position",
                            blocks.ChoiceBlock(
                                choices=[
                                    ("left", "Izquierda"),
                                    ("right", "Derecha"),
                                ],
                                default="left",
                            ),
                        ),
                    ]
                ),
            ),

            # video segment
            (
                "video_segment",
                blocks.StructBlock(
                    [
                        ("url", blocks.URLBlock(blank=True), ),
                    ]
                ),
            ),

            (
                "information_segment",
                blocks.StructBlock(
                    [
                        ("list_information", blocks.ListBlock(InformationBlock) )
                        
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=False,
        max_num=1,
    )

    content_panels = Page.content_panels + [
        FieldPanel("order"),
        FieldPanel("segments"),
    ]
