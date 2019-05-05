# Generated by Django 2.1.7 on 2019-04-17 09:44

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('taxonomy', '0008_auto_20190408_2246'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(blank=True, default=True, verbose_name='Status')),
                ('active_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('inactive_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('order_value', models.IntegerField(blank=True, unique=True, verbose_name='Order value')),
                ('url', models.URLField(verbose_name='Url')),
                ('show_in_home_page', models.BooleanField(default=False, verbose_name='Show in home page')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Short description')),
                ('is_live', models.BooleanField(verbose_name='Is Live')),
                ('url_of_replay', models.URLField(verbose_name='Url of replay')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_multimedia.stream_set+', to='contenttypes.ContentType')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxonomy.Section')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(blank=True, default=True, verbose_name='Status')),
                ('active_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('inactive_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('order_value', models.IntegerField(blank=True, unique=True, verbose_name='Order value')),
                ('url', models.URLField(verbose_name='Url')),
                ('show_in_home_page', models.BooleanField(default=False, verbose_name='Show in home page')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Short description')),
                ('auto_play', models.BooleanField(verbose_name='Auto play')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_multimedia.video_set+', to='contenttypes.ContentType')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxonomy.Section')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]