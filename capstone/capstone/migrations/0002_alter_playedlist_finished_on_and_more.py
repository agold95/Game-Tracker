# Generated by Django 4.1.6 on 2023-04-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playedlist',
            name='finished_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='playinglist',
            name='started_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
