# Generated by Django 2.1.7 on 2019-04-27 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0020_auto_20190427_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='soccervideo',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sports.SoccerMatch'),
            preserve_default=False,
        ),
    ]
