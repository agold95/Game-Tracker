# Generated by Django 4.1.6 on 2023-04-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0005_alter_playedlist_finished_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playedlist',
            name='finished_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='playinglist',
            name='started_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]