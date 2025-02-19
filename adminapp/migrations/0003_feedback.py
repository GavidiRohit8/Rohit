# Generated by Django 5.0.7 on 2024-10-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0002_studentlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("username", models.CharField(max_length=10, unique=True)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=10, unique=True)),
                ("text_field", models.CharField(max_length=150, unique=True)),
            ],
        ),
    ]
