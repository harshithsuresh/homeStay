# Generated by Django 3.2.6 on 2021-08-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0002_auto_20210811_1508'),
        ('review', '0004_auto_20210811_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='stayTitle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stays.stay'),
        ),
    ]
