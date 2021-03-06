# Generated by Django 2.2.7 on 2020-02-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0010_jeu_configuration'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgue',
            name='tirage_commentaire',
            field=models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('mecanique_suspendue', 'Mécanique suspendue'), ('mecanique_barker', 'Mécanique Barker'), ('pneumatique', 'Pneumatique'), ('electrique', 'Electrique')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orgue',
            name='transmission_commentaire',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
