# Generated by Django 2.1.7 on 2019-04-19 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0010_auto_20190419_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebooklivestreamgroup',
            name='facebook_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multimedia.FacebookGroup'),
        ),
        migrations.AlterField(
            model_name='facebooklivestreamgroup',
            name='facebook_stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multimedia.FacebookStream'),
        ),
        migrations.AlterField(
            model_name='facebooklivestreampage',
            name='facebook_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multimedia.FacebookPage'),
        ),
        migrations.AlterField(
            model_name='facebooklivestreampage',
            name='facebook_stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multimedia.FacebookStream'),
        ),
    ]
