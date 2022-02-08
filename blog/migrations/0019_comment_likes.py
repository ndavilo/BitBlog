# Generated by Django 4.0 on 2022-02-07 14:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_alter_comment_options_comment_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='blog_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]