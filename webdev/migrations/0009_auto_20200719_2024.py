# Generated by Django 3.0.7 on 2020-07-19 20:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0008_auto_20200719_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdevproject',
            name='display_image',
            field=wagtail.core.fields.StreamField([('WebProject', wagtail.core.blocks.StructBlock([('demo_laptop_display', wagtail.images.blocks.ImageChooserBlock(required=True)), ('demo_mobile_display', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('StandardProject', wagtail.core.blocks.StructBlock([('demo_display', wagtail.images.blocks.ImageChooserBlock(required=True))]))]),
        ),
    ]