# Generated by Django 3.2.6 on 2021-08-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquires', '0013_auto_20210815_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquire',
            name='name',
        ),
    ]