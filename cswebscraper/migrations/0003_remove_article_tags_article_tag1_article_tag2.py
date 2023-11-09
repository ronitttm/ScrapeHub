# Generated by Django 4.2.6 on 2023-11-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cswebscraper", "0002_article_tags"),
    ]

    operations = [
        migrations.RemoveField(model_name="article", name="tags",),
        migrations.AddField(
            model_name="article",
            name="tag1",
            field=models.CharField(default="Null", max_length=200),
        ),
        migrations.AddField(
            model_name="article",
            name="tag2",
            field=models.CharField(default="Null", max_length=200),
        ),
    ]
