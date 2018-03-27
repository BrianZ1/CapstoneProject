# Generated by Django 2.0.2 on 2018-03-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports', '0003_auto_20180306_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
