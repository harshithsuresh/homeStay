# Generated by Django 3.2.6 on 2021-08-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0002_auto_20210811_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='stay',
            name='avgReview',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stay',
            name='countReview',
            field=models.IntegerField(default=1),
        ),
    ]
