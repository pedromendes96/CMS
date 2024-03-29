# Generated by Django 2.1.7 on 2019-04-08 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_auto_20190408_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='category',
            name='section',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='categorytag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='categorytag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='section',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CategoryTag',
        ),
        migrations.DeleteModel(
            name='HistoricalCategory',
        ),
    ]
