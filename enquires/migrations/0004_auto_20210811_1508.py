# Generated by Django 3.2.6 on 2021-08-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquires', '0003_auto_20210811_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquire',
            name='bookingDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='enquire',
            name='closingDate',
            field=models.DateField(),
        ),
    ]
