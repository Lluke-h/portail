# Generated by Django 2.2.7 on 2020-01-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0003_orgue_boite_expressive'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgue',
            name='code_departement',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orgue',
            name='osm_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orgue',
            name='osm_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orgue',
            name='osm_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orgue',
            name='osm_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orgue',
            name='references_palissy',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='type',
            field=models.CharField(choices=[('construction', 'Construction'), ('reconstruction', 'Reconstruction'), ('destruction', 'Destruction'), ('restauration', 'Restauration'), ('deplacement', 'Déplacement'), ('relevage', 'Relevage'), ('disparition', 'Disparition'), ('degats', 'Dégâts'), ('classement_mh', 'Classement aux monuments historiques'), ('inscription_mh', 'Inscription aux monuments historiques')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='boite_expressive',
            field=models.BooleanField(default=False, verbose_name="Est-ce que l'orgue a une boîte expressive ?"),
        ),
    ]
