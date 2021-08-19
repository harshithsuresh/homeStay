# Generated by Django 3.2.6 on 2021-08-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0002_auto_20210811_1508'),
        ('enquires', '0004_auto_20210811_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquire',
            name='stayID',
        ),
        migrations.AddField(
            model_name='enquire',
            name='stay',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='stays.stay'),
        ),
        migrations.AlterField(
            model_name='enquire',
            name='bookingDate',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='enquire',
            name='closingDate',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='enquire',
            name='userID',
            field=models.IntegerField(default=True),
        ),
    ]
