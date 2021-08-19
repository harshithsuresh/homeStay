# Generated by Django 3.2.6 on 2021-08-11 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0002_auto_20210811_1508'),
        ('review', '0002_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stayID',
        ),
        migrations.RemoveField(
            model_name='review',
            name='userID',
        ),
        migrations.AddField(
            model_name='review',
            name='stayTitle',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='stays.stay'),
        ),
        migrations.AddField(
            model_name='review',
            name='userName',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]