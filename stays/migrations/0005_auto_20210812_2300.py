# Generated by Django 3.2.6 on 2021-08-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0004_auto_20210812_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='avgReview',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stay',
            name='countReview',
            field=models.IntegerField(blank=True),
        ),
    ]