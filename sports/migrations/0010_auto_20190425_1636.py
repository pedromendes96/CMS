# Generated by Django 2.1.7 on 2019-04-25 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0009_apifootballcoach_apifootballplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiFootballStanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(blank=True, default=True, verbose_name='Status')),
                ('active_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('inactive_at', models.DateTimeField(blank=True, null=True, verbose_name='Inactive at')),
                ('sort_order', models.IntegerField(blank=True, unique=True, verbose_name='Order value')),
                ('rank', models.IntegerField()),
                ('matchsPlayed', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lose', models.IntegerField()),
                ('goalsFor', models.IntegerField()),
                ('goalsAgainst', models.IntegerField()),
                ('goalsDiff', models.IntegerField()),
                ('points', models.IntegerField()),
                ('group', models.CharField(max_length=256)),
                ('lastUpdate', models.CharField(max_length=256)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballTeam')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='apifootballstading',
            name='league',
        ),
        migrations.RemoveField(
            model_name='apifootballstading',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='apifootballteamstading',
            name='stading',
        ),
        migrations.RemoveField(
            model_name='apifootballteamstading',
            name='team',
        ),
        migrations.DeleteModel(
            name='ApiFootballStading',
        ),
        migrations.DeleteModel(
            name='ApiFootballTeamStading',
        ),
    ]