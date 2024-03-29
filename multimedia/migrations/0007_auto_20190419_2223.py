# Generated by Django 2.1.7 on 2019-04-19 22:23

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('multimedia', '0006_auto_20190419_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagManagment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='media',
            options={},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={},
        ),
        migrations.AddField(
            model_name='tagmanagment',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='multimedia.Media'),
        ),
        migrations.AddField(
            model_name='tagmanagment',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multimedia_tagmanagment_items', to='taggit.Tag'),
        ),
    ]
