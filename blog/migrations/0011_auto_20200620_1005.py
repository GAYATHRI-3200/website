# Generated by Django 3.0.7 on 2020-06-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200619_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
