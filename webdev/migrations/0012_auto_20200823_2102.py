# Generated by Django 3.0.7 on 2020-08-23 21:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0011_projectdetailpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetailpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('single_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('double_image', wagtail.core.blocks.StructBlock([('image_left', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_right', wagtail.images.blocks.ImageChooserBlock(required=True))]))]),
        ),
    ]