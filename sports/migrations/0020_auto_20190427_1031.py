# Generated by Django 2.1.7 on 2019-04-27 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0019_auto_20190427_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apifootballstanding',
            old_name='goalsAgainst',
            new_name='goals_against',
        ),
        migrations.RenameField(
            model_name='apifootballstanding',
            old_name='goalsDiff',
            new_name='goals_diff',
        ),
        migrations.RenameField(
            model_name='apifootballstanding',
            old_name='goalsFor',
            new_name='goals_for',
        ),
        migrations.RenameField(
            model_name='apifootballstanding',
            old_name='lastUpdate',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='apifootballstanding',
            old_name='matchsPlayed',
            new_name='matchs_played',
        ),
    ]
