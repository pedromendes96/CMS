# Generated by Django 2.1.7 on 2019-04-25 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0007_auto_20190425_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='apifootballteam',
            name='league',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballLeague'),
            preserve_default=False,
        ),
    ]