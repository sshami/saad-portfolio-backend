# Generated by Django 3.0.7 on 2020-07-19 19:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0004_auto_20200719_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='webdev',
            name='featured_projects',
            field=wagtail.core.fields.StreamField([('Project', wagtail.core.blocks.PageChooserBlock(page_type=['webdev.WebdevProject']))], blank=True),
        ),
    ]
