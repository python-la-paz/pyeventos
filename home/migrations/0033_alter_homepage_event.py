# Generated by Django 4.1.7 on 2023-09-25 01:36

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0032_homepage_position_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="event",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
