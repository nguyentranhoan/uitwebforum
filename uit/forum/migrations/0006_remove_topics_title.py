# Generated by Django 3.0.7 on 2020-06-13 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20200613_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='title',
        ),
    ]
