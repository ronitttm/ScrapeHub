# Generated by Django 4.2.5 on 2023-11-09 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cswebscraper', '0003_remove_article_tags_article_tag1_article_tag2'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]