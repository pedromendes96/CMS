# Generated by Django 2.1.7 on 2019-04-18 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publish Date'),
        ),
    ]
