# Generated by Django 3.0.7 on 2020-06-17 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200617_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='slug',
            new_name='Slug',
        ),
    ]
