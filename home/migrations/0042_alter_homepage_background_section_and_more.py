# Generated by Django 5.0.9 on 2024-10-02 01:43

import wagtail_color_panel.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_homepage_externalraws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='background_section',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FFFFFF', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='color_gradient_1',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FF4D79', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='color_gradient_2',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FF809F', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='color_primary',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#ff4a67', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='color_text_hero',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FFFFFF', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='color_text_section',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FFFFFF', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='navbar_background',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#000000', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='navbar_links_color',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FFFFFF', max_length=250),
        ),
        migrations.AlterField(
            model_name='segmentpage',
            name='background_section',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#FFFFFF', max_length=250),
        ),
        migrations.AlterField(
            model_name='segmentpage',
            name='color_text_section',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#000000', max_length=250),
        ),
    ]