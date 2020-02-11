# Generated by Django 2.2.7 on 2020-02-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0014_auto_20200211_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgue',
            name='association',
        ),
        migrations.RemoveField(
            model_name='orgue',
            name='association_lien',
        ),
        migrations.AddField(
            model_name='orgue',
            name='lien_reference',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien de référence'),
        ),
        migrations.AddField(
            model_name='orgue',
            name='organisme',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name="Organisme auquel s'adresser"),
        ),
    ]
