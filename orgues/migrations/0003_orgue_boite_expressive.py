# Generated by Django 2.2.7 on 2020-01-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0002_auto_20191216_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgue',
            name='boite_expressive',
            field=models.BooleanField(default=False, verbose_name="Est-ce que l'orgue a une boîte expressive"),
        ),
    ]
