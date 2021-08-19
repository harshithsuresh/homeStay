# Generated by Django 3.2.6 on 2021-08-11 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0002_auto_20210811_1508'),
        ('review', '0003_auto_20210811_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='stayTitle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stays.stay'),
        ),
        migrations.AlterField(
            model_name='review',
            name='userName',
            field=models.CharField(max_length=30),
        ),
    ]
