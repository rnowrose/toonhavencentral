# Generated by Django 5.1.1 on 2024-11-03 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cover",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("height", models.IntegerField()),
                ("image_id", models.CharField()),
                ("url", models.CharField()),
                ("width", models.IntegerField()),
                ("alpha_channel", models.BooleanField()),
                ("animated", models.BooleanField()),
            ],
            options={
                "db_table": "cover",
            },
        ),
        migrations.CreateModel(
            name="Franchise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("name", models.CharField(max_length=100)),
                ("slug", models.CharField(max_length=100)),
                ("url", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "franchise",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                ("url", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "genre",
            },
        ),
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("name", models.CharField(max_length=255)),
                ("abbreviation", models.CharField(max_length=255)),
                ("alternative_name", models.CharField(max_length=255)),
                (
                    "category",
                    models.SmallIntegerField(
                        choices=[
                            (0, "----"),
                            (1, "Console"),
                            (2, "Arcade"),
                            (3, "Platform"),
                            (4, "Operating System"),
                            (5, "Portable Console"),
                            (6, "Computer"),
                        ],
                        default=0,
                    ),
                ),
                ("generation", models.IntegerField()),
                ("slug", models.CharField(max_length=255)),
                ("summary", models.TextField()),
                ("url", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "platform",
            },
        ),
        migrations.CreateModel(
            name="PlatformLogo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("height", models.IntegerField()),
                ("image_id", models.CharField()),
                ("url", models.CharField()),
                ("width", models.IntegerField()),
                ("alpha_channel", models.BooleanField()),
                ("animated", models.BooleanField()),
            ],
            options={
                "db_table": "platform_logo",
            },
        ),
        migrations.CreateModel(
            name="PlayerPerspectives",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("name", models.CharField(max_length=200)),
                ("slug", models.CharField(max_length=200)),
                ("url", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "player_perspectives",
            },
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=128)),
                ("url", models.CharField(max_length=128)),
                ("summary", models.TextField()),
                ("storyline", models.TextField()),
                ("collections", models.JSONField()),
                ("franchises", models.JSONField()),
                (
                    "aggregated_rating",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                ("aggregated_rating_count", models.IntegerField()),
                ("bundles", models.JSONField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            (0, "Released"),
                            (2, "Alpha"),
                            (3, "Beta"),
                            (4, "Early Access"),
                            (5, "Offline"),
                            (6, "Cancelled"),
                            (7, "Rumored"),
                            (8, "Delisted"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            (0, "Main Game"),
                            (1, "DLC Addon"),
                            (2, "Expansion"),
                            (3, "Bundle"),
                            (4, "Standalone Expansion"),
                            (5, "Mod"),
                            (6, "Episode"),
                            (7, "Season"),
                            (8, "Remake"),
                            (9, "Remaster"),
                            (10, "Expanded Game"),
                            (11, "Port"),
                            (12, "Fork"),
                            (13, "Pack"),
                            (14, "Update"),
                        ],
                        max_length=10,
                    ),
                ),
                ("dlcs", models.JSONField()),
                ("hypes", models.IntegerField()),
                ("ports", models.JSONField()),
                ("rating", models.DecimalField(decimal_places=2, max_digits=6)),
                ("rating_count", models.IntegerField()),
                ("remakes", models.JSONField()),
                ("remasters", models.JSONField()),
                ("similar_games", models.JSONField()),
                ("standalone_expansions", models.JSONField()),
                ("total_rating", models.DecimalField(decimal_places=2, max_digits=6)),
                ("total_rating_count", models.IntegerField()),
                ("platform", models.JSONField()),
                ("screenshots", models.JSONField()),
                (
                    "cover",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cover",
                        to="app.cover",
                    ),
                ),
                (
                    "franchise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="franchises",
                        to="app.franchise",
                    ),
                ),
                (
                    "version_parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parent_game",
                        to="app.game",
                    ),
                ),
                (
                    "player_perspectives",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player_perspectives",
                        to="app.playerperspectives",
                    ),
                ),
            ],
            options={
                "db_table": "game",
            },
        ),
        migrations.AddField(
            model_name="cover",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="games",
                to="app.game",
            ),
        ),
        migrations.CreateModel(
            name="Screenshot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("checksum", models.UUIDField()),
                ("height", models.IntegerField()),
                ("image_id", models.CharField()),
                ("url", models.CharField()),
                ("width", models.IntegerField()),
                ("alpha_channel", models.BooleanField()),
                ("animated", models.BooleanField()),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="game_screenshots",
                        to="app.game",
                    ),
                ),
            ],
            options={
                "db_table": "screenshot",
            },
        ),
    ]
