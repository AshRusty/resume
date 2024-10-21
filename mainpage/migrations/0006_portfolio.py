# Generated by Django 5.1.2 on 2024-10-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainpage", "0005_workexperience"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
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
                (
                    "image",
                    models.ImageField(upload_to="portfolio", verbose_name="Картинка"),
                ),
                (
                    "image_mobile",
                    models.ImageField(
                        upload_to="portfolio", verbose_name="Картинка для мобилки"
                    ),
                ),
                (
                    "project_name",
                    models.CharField(max_length=255, verbose_name="Название проекта"),
                ),
                (
                    "github_link",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Ссылка на гитхаб проекта",
                    ),
                ),
                (
                    "live_demo",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ссылка на демо"
                    ),
                ),
            ],
            options={
                "verbose_name": "Проект",
                "verbose_name_plural": "Проекты",
            },
        ),
    ]
