# Generated by Django 3.0.7 on 2020-10-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_linkedin',
            field=models.URLField(blank=True, verbose_name='Linkedin'),
        ),
    ]
