# Generated by Django 4.1.7 on 2023-09-24 18:01

from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0029_alter_segmentpage_segments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="footer_networks",
            field=wagtail.fields.StreamField(
                [
                    (
                        "networks",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "classname",
                                    wagtail.blocks.CharBlock(
                                        max_length=250, required=True
                                    ),
                                ),
                                (
                                    "lni_icon",
                                    wagtail.blocks.CharBlock(
                                        help_text="(lni lni-help) https://lineicons.com/icons/",
                                        required=True,
                                    ),
                                ),
                                ("url", wagtail.blocks.URLBlock(required=True)),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="menu_links",
            field=wagtail.fields.StreamField(
                [
                    (
                        "menu_links",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        max_length=250, required=True
                                    ),
                                ),
                                (
                                    "url",
                                    wagtail.blocks.CharBlock(
                                        default="#", max_length=250, required=True
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="segmentpage",
            name="segments",
            field=wagtail.fields.StreamField(
                [
                    (
                        "detail_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        blank=False, max_length=250
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "list_options",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.RichTextBlock(required=False)
                                    ),
                                ),
                                ("url", wagtail.blocks.URLBlock(required=False)),
                                (
                                    "url_text",
                                    wagtail.blocks.CharBlock(
                                        default="More info",
                                        max_length=250,
                                        required=False,
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "position",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Izquierda"),
                                            ("right", "Derecha"),
                                            ("full", "Completa"),
                                            ("empty", "Sin Imagen"),
                                        ]
                                    ),
                                ),
                                (
                                    "list_style",
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video_segment",
                        wagtail.blocks.StructBlock(
                            [("url", wagtail.blocks.URLBlock(blank=True))]
                        ),
                    ),
                    (
                        "information_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "id_tag",
                                    wagtail.blocks.CharBlock(
                                        default="contact-text",
                                        max_length=250,
                                        required=False,
                                    ),
                                ),
                                (
                                    "class_name",
                                    wagtail.blocks.CharBlock(
                                        default="contact-wrapper",
                                        max_length=250,
                                        required=False,
                                    ),
                                ),
                                (
                                    "list_information",
                                    wagtail.blocks.ListBlock(
                                        home.models.InformationBlock, max_num=4
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "sponsor_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        default="Sponsors",
                                        max_length=250,
                                        required=True,
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "background",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "sponsors",
                                    wagtail.blocks.ListBlock(home.models.SponsorBlock),
                                ),
                            ]
                        ),
                    ),
                    (
                        "maps_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        blank=True,
                                        help_text="https://www.google.com/maps/embed?pb=.....",
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "pricing_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        default="Pricing", max_length=250, required=True
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "tiers",
                                    wagtail.blocks.ListBlock(home.models.TiersBlock),
                                ),
                            ]
                        ),
                    ),
                    (
                        "schedule_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        default="Schedule",
                                        max_length=250,
                                        required=True,
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "schedules",
                                    wagtail.blocks.ListBlock(home.models.ScheduleBlock),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
