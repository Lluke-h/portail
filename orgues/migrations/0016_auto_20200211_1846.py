# Generated by Django 2.2.7 on 2020-02-11 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0015_auto_20200211_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgue',
            name='osm_latitude',
        ),
        migrations.RemoveField(
            model_name='orgue',
            name='osm_longitude',
        ),
    ]
