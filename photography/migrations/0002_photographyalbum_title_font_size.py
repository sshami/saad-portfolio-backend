# Generated by Django 3.0.7 on 2020-06-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographyalbum',
            name='title_font_size',
            field=models.DecimalField(decimal_places=2, default=12.5, max_digits=5, verbose_name='Title Font Size'),
        ),
    ]