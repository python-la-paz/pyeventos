# Generated by Django 4.1.7 on 2023-09-25 02:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0034_homepage_color_text_hero"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="hero_padding_left",
            field=models.CharField(default="20px", max_length=250),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_padding_right",
            field=models.CharField(default="20px", max_length=250),
        ),
    ]