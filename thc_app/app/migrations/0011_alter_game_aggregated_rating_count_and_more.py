# Generated by Django 5.1.1 on 2024-11-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_remove_game_platforms_remove_game_screenshots_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="aggregated_rating_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="game",
            name="bundles",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="collections",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="dlcs",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="franchises",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="hypes",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="game",
            name="ports",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="rating_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="game",
            name="remakes",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="remasters",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="similar_games",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="standalone_expansions",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="game",
            name="storyline",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="summary",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="total_rating_count",
            field=models.IntegerField(default=0),
        ),
    ]
