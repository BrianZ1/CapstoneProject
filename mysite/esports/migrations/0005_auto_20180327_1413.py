# Generated by Django 2.0.2 on 2018-03-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports', '0004_event_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
