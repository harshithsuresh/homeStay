# Generated by Django 3.2.6 on 2021-08-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0003_auto_20210811_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
