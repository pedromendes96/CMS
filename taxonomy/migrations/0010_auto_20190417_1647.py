# Generated by Django 2.1.7 on 2019-04-17 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0009_auto_20190417_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='order_value',
            new_name='sort_order',
        ),
        migrations.RenameField(
            model_name='historicalcategory',
            old_name='order_value',
            new_name='sort_order',
        ),
        migrations.RenameField(
            model_name='historicalsection',
            old_name='order_value',
            new_name='sort_order',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='order_value',
            new_name='sort_order',
        ),
    ]
