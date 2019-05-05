# Generated by Django 2.1.7 on 2019-04-19 22:18

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0005_auto_20190419_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]