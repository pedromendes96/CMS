# Generated by Django 2.1.7 on 2019-04-08 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190408_2253'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('newsletter', '0005_newslettermessage_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='newslettermessage',
            name='template',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
    ]
