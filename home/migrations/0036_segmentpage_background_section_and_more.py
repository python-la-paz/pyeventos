# Generated by Django 4.1.7 on 2023-09-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0035_homepage_hero_padding_left_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="segmentpage",
            name="background_section",
            field=models.CharField(blank=True, default="#FFFFFF", max_length=250),
        ),
        migrations.AddField(
            model_name="segmentpage",
            name="color_text_section",
            field=models.CharField(blank=True, default="black", max_length=250),
        ),
    ]
