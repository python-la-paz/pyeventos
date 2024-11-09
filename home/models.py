from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.fields import ColorField


class HomePage(Page):
    event = RichTextField(blank=True)
    position_event = models.CharField(
        max_length=250,
        choices=[
            ("center", "center"),
            ("left", "left"),
            ("right", "right"),
        ],
        default="center",
    )
    about = RichTextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    literal_date = models.CharField(max_length=250, blank=True)
    url_get_tickets = models.URLField(blank=True)
    text_get_tickets = models.CharField(
        max_length=250, blank=True, default="Get tickets"
    )
    event_date = models.DateField(blank=True, null=True)

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    logo_image_big = models.ForeignKey(
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
    hero_image_overlay_opacity = models.DecimalField(
        default=0.70, decimal_places=2, max_digits=3
    )
    hero_padding_left = models.CharField(max_length=250, default="20px")
    hero_padding_right = models.CharField(max_length=250, default="20px")
    footer_title = models.CharField(max_length=250, blank=True)
    footer_site_info = RichTextField(blank=True)
    footer_networks = StreamField(
        [
            (
                "networks",
                blocks.StructBlock(
                    [
                        ("classname", blocks.CharBlock(max_length=250, required=True)),
                        (
                            "lni_icon",
                            blocks.CharBlock(
                                help_text="(lni lni-help) https://lineicons.com/icons/",
                                required=True,
                            ),
                        ),
                        (
                            "url",
                            blocks.URLBlock(required=True),
                        ),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
    )

    primaryFontURL = models.URLField(max_length=250, blank=True)
    primaryFontFamily = models.CharField(max_length=250, default="sans-serif")
    secondaryFontURL = models.URLField(max_length=250, blank=True)
    secondaryFontFamily = models.CharField(max_length=250, default="sans-serif")
    color_gradient_1 = ColorField(max_length=250, blank=True, default="#FF4D79")
    color_gradient_2 = ColorField(max_length=250, blank=True, default="#FF809F")
    color_primary = ColorField(max_length=250, blank=True, default="#ff4a67")
    color_text_hero = ColorField(max_length=250, blank=True, default="#FFFFFF")

    show_time = models.BooleanField(default=True)
    background_section = ColorField(max_length=250, blank=True, default="#FFFFFF")
    color_text_section = ColorField(max_length=250, blank=True, default="#FFFFFF")
    navbar_background = ColorField(max_length=250, blank=True, default="#000000")
    navbar_links_color = ColorField(max_length=250, blank=True, default="#FFFFFF")
    message_show_time = models.CharField(
        max_length=250, blank=True, default="Próximamente..."
    )
    menu_links = StreamField(
        [
            (
                "menu_links",
                blocks.StructBlock(
                    [
                        ("text", blocks.CharBlock(max_length=250, required=True)),
                        (
                            "url",
                            blocks.CharBlock(
                                max_length=250, required=True, default="#"
                            ),
                        ),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
    )
    favicon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="max size 256x256 png format",
    )
    footer_background = models.CharField(max_length=250, blank=True, default="#161E26")
    footer_color_text = models.CharField(max_length=250, blank=True, default="#9e9e9e")
    externalRaws = StreamField(
        [
            (
                "external",
                blocks.StructBlock(
                    [
                        ("rawHTML", blocks.RawHTMLBlock(required=False)),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("event"),
        FieldPanel("favicon"),
        NativeColorPanel("navbar_background"),
        NativeColorPanel("navbar_links_color"),
        FieldPanel("position_event"),
        FieldPanel("about"),
        FieldPanel("location"),
        FieldPanel("literal_date"),
        FieldPanel("url_get_tickets"),
        FieldPanel("text_get_tickets"),
        FieldPanel("event_date"),
        FieldPanel("logo_image"),
        FieldPanel("logo_image_big"),
        FieldPanel("hero_image"),
        FieldPanel("hero_image_overlay_opacity"),
        NativeColorPanel("color_text_hero"),
        FieldPanel("hero_padding_left"),
        FieldPanel("hero_padding_right"),
        FieldPanel("primaryFontURL"),
        FieldPanel("primaryFontFamily"),
        FieldPanel("secondaryFontURL"),
        FieldPanel("secondaryFontFamily"),
        NativeColorPanel("color_gradient_1"),
        NativeColorPanel("color_gradient_2"),
        NativeColorPanel("color_primary"),
        FieldPanel("show_time"),
        NativeColorPanel("background_section"),
        NativeColorPanel("color_text_section"),
        FieldPanel("message_show_time"),
        FieldPanel("menu_links"),
        FieldPanel("footer_title"),
        FieldPanel("footer_site_info"),
        FieldPanel("footer_networks"),
        NativeColorPanel("footer_background"),
        NativeColorPanel("footer_color_text"),
        FieldPanel("externalRaws"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        segments = SegmentPage.objects.child_of(self).live().order_by("order")
        context["segments"] = segments  # sorted (segments, key=lambda x: x.order)
        context["exist_descendants"] = [
            descendant
            for descendant in self.get_descendants()
            if descendant.live and descendant.content_type == self.content_type
        ]
        return context


class InformationBlock(blocks.StructBlock):
    lni_icon = blocks.CharBlock(help_text="(lni lni-help) https://lineicons.com/icons/")
    title = blocks.CharBlock()
    description = blocks.CharBlock()


class SponsorBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    level = blocks.ChoiceBlock(
        choices=[
            ("silver", "Plata"),
            ("gold", "Oro"),
            ("diamond", "Diamante"),
        ],
        default="silver",
    )
    url = blocks.URLBlock(required=False)


class TiersBlock(blocks.StructBlock):
    classname = blocks.CharBlock(required=False)
    name = blocks.CharBlock()
    pricing = blocks.CharBlock()
    detail_pricing = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    benefits = blocks.ListBlock(blocks.CharBlock(required=False))
    no_benefits = blocks.ListBlock(blocks.CharBlock(required=False))
    url = blocks.URLBlock(required=False)
    url_text = blocks.CharBlock(required=False, default="Buy now")
    bg_color = blocks.CharBlock(required=False, default="#fff")


class ScheduleDetailBlock(blocks.StructBlock):
    menu_title = blocks.CharBlock()
    menu_subtitle = blocks.CharBlock(default="Workshop")

    title = blocks.CharBlock()
    speaker = blocks.CharBlock()
    resume = blocks.RichTextBlock()
    location = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)


class ScheduleBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    detail = blocks.CharBlock()
    schedule_details = blocks.ListBlock(ScheduleDetailBlock(required=False))


class SegmentPage(Page):
    order = models.IntegerField(default=0)
    background_section = ColorField(max_length=250, blank=True, default="#FFFFFF")
    color_text_section = ColorField(max_length=250, blank=True, default="#000000")
    segments = StreamField(
        [
            # detail segment
            (
                "detail_segment",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock(max_length=250, blank=False)),
                        ("description", blocks.RichTextBlock(required=False)),
                        (
                            "list_options",
                            blocks.ListBlock(blocks.RichTextBlock(required=False)),
                        ),
                        ("url", blocks.URLBlock(required=False)),
                        (
                            "url_text",
                            blocks.CharBlock(
                                max_length=250, required=False, default="More info"
                            ),
                        ),
                        ("image", ImageChooserBlock(required=False)),
                        (
                            "position",
                            blocks.ChoiceBlock(
                                choices=[
                                    ("left", "Izquierda"),
                                    ("right", "Derecha"),
                                    ("full", "Completa"),
                                    ("empty", "Sin Imagen"),
                                ],
                                default="left",
                            ),
                        ),
                        (
                            "list_style",
                            blocks.BooleanBlock(required=False, default=False),
                        ),
                    ]
                ),
            ),
            # video segment
            (
                "video_segment",
                blocks.StructBlock(
                    [
                        (
                            "url",
                            blocks.URLBlock(blank=True),
                        ),
                    ]
                ),
            ),
            (
                "information_segment",
                blocks.StructBlock(
                    [
                        (
                            "id_tag",
                            blocks.CharBlock(
                                max_length=250, required=False, default="contact-text"
                            ),
                        ),
                        (
                            "class_name",
                            blocks.CharBlock(
                                max_length=250,
                                required=False,
                                default="contact-wrapper",
                            ),
                        ),
                        (
                            "list_information",
                            blocks.ListBlock(InformationBlock, max_num=4),
                        ),
                    ]
                ),
            ),
            (
                "sponsor_segment",
                blocks.StructBlock(
                    [
                        (
                            "name",
                            blocks.CharBlock(
                                max_length=250, required=True, default="Sponsors"
                            ),
                        ),
                        ("description", blocks.RichTextBlock(required=False)),
                        ("background", ImageChooserBlock(required=False)),
                        ("sponsors", blocks.ListBlock(SponsorBlock)),
                    ]
                ),
            ),
            (
                "maps_segment",
                blocks.StructBlock(
                    [
                        (
                            "url",
                            blocks.URLBlock(
                                blank=True,
                                help_text="https://www.google.com/maps/embed?pb=.....",
                            ),
                        ),
                    ]
                ),
            ),
            (
                "pricing_segment",
                blocks.StructBlock(
                    [
                        (
                            "name",
                            blocks.CharBlock(
                                max_length=250, required=True, default="Pricing"
                            ),
                        ),
                        ("description", blocks.RichTextBlock(required=False)),
                        ("tiers", blocks.ListBlock(TiersBlock)),
                    ]
                ),
            ),
            (
                "schedule_segment",
                blocks.StructBlock(
                    [
                        (
                            "name",
                            blocks.CharBlock(
                                max_length=250, required=True, default="Schedule"
                            ),
                        ),
                        ("description", blocks.RichTextBlock(required=False)),
                        ("schedules", blocks.ListBlock(ScheduleBlock)),
                    ]
                ),
            ),
            (
                "iframe_segment",
                blocks.StructBlock(
                    [
                        (
                            "rawHTML",
                            blocks.RawHTMLBlock(
                                required=False,
                                help_text='&lt;div style="overflow-x:auto; max-height: 30vh;" &gt;&lt;content&gt; ... &lt;/content&gt; &lt;/div&gt;',
                            ),
                        ),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
        max_num=1,
    )

    content_panels = Page.content_panels + [
        FieldPanel("order"),
        NativeColorPanel("color_text_section"),
        FieldPanel("segments"),
        NativeColorPanel("background_section"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["parent"] = self.get_parent().specific
        return context
