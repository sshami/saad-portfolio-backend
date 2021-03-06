# Generated by Django 3.0.7 on 2020-07-19 19:20

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('webdev', '0002_auto_20200719_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebdevProject',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('summary', models.CharField(max_length=255)),
                ('display_image', wagtail.core.fields.StreamField([('WebProject', wagtail.core.blocks.StructBlock([('demo_laptop_display', wagtail.images.blocks.ImageChooserBlock(required=True)), ('demo_mobile_display', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('StandardProject', wagtail.core.blocks.StructBlock([('demo_display', wagtail.images.blocks.ImageChooserBlock(required=True))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
