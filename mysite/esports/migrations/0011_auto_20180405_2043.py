# Generated by Django 2.0.2 on 2018-04-06 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esports', '0010_auto_20180405_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='game',
        ),
        migrations.RemoveField(
            model_name='player',
            name='game',
        ),
    ]
