# Generated by Django 2.2.7 on 2020-02-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0004_auto_20200124_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evenement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='orgue',
            name='description',
        ),
        migrations.AddField(
            model_name='evenement',
            name='resume',
            field=models.TextField(blank=True, help_text='700 caractères max', max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='orgue',
            name='resume',
            field=models.TextField(blank=True, help_text="Présentation en quelques lignes de l'instrument et son originalité (max 500 caractères)", max_length=500, verbose_name='Resumé'),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='type',
            field=models.CharField(choices=[('construction', 'Construction'), ('reconstruction', 'Reconstruction'), ('destruction', 'Destruction'), ('restauration', 'Restauration'), ('deplacement', 'Déplacement'), ('relevage', 'Relevage'), ('disparition', 'Disparition'), ('degats', 'Dégâts'), ('classement_mh', 'Classement au titre des monuments historiques'), ('inscription_mh', 'Inscription au titre des monuments historiques')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='buffet',
            field=models.TextField(blank=True, help_text='Description du buffet et de son état.', null=True, verbose_name='Description buffet'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='commentaire_admin',
            field=models.TextField(blank=True, help_text='Commentaire uniquement visible par les rédacteurs', null=True, verbose_name='Commentaire rédacteurs'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='commentaire_tuyauterie',
            field=models.TextField(blank=True, help_text='Syntaxe markdown supportée'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='console',
            field=models.TextField(blank=True, help_text="Description de la console (ex: en fenêtre, séparée organiste tourné vers l'orgue ...).", null=True, verbose_name='Description console'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='osm_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Id open street map'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='osm_latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude open street map'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='osm_longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude open street map'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='osm_type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Type open street map'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='references_palissy',
            field=models.CharField(blank=True, help_text='Séparer les codes par des virgules', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='sommiers',
            field=models.TextField(blank=True, help_text='Syntaxe markdown supportée', null=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='soufflerie',
            field=models.TextField(blank=True, help_text='Syntaxe markdown supportée', null=True),
        ),
    ]
