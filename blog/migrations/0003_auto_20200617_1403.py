# Generated by Django 3.0.7 on 2020-06-17 08:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200616_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
