# Generated by Django 4.2.5 on 2023-09-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="", max_length=25),
        ),
    ]
