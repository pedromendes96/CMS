# Generated by Django 2.1.7 on 2019-04-08 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='CommentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('inactive_at', models.DateTimeField(blank=True, null=True, verbose_name='Active at')),
                ('order_value', models.IntegerField(blank=True, unique=True, verbose_name='Order value')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('refused', 'Refused')], default='draft', max_length=32, verbose_name='status')),
                ('active', models.BooleanField(blank=True, default=False, verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NormalComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.Comment')),
                ('is_spam', models.BooleanField(default=False, verbose_name='Is spam')),
                ('marked_as_spam_at', models.DateTimeField(blank=True, null=True, verbose_name='Marked as spam at')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('comments.comment',),
        ),
        migrations.CreateModel(
            name='ProfessionalComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.Comment')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('comments.comment',),
        ),
        migrations.CreateModel(
            name='ReporterComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.Comment')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('comments.comment',),
        ),
        migrations.AddField(
            model_name='comment',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', related_query_name='children', to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='comment',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_comments.comment_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', related_query_name='comment', to='comments.CommentStatus', verbose_name='Comment status'),
        ),
    ]