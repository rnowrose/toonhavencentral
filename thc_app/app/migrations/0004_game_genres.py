# Generated by Django 5.1.1 on 2024-11-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_gamewebsite"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="genres",
            field=models.JSONField(default=list),
        ),
    ]
