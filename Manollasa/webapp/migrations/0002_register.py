# Generated by Django 4.1.6 on 2023-02-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="register",
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
                ("Name", models.CharField(max_length=100)),
                ("Email", models.CharField(max_length=100)),
                ("Place", models.CharField(max_length=100)),
                ("Phone", models.CharField(max_length=100)),
                (
                    "Branch",
                    models.CharField(
                        choices=[
                            ("BA", "BA"),
                            ("BBA", "BBA"),
                            ("BLIS", "BLIS"),
                            ("MA", "MA"),
                            ("MEDICAL", "MEDICAL"),
                            ("MBA", "MBA"),
                            ("BOSSE", "BOSSE"),
                            ("BCOM", "BCOM"),
                            ("BSC", "BSC"),
                            ("BSW", "BSW"),
                        ],
                        max_length=10,
                    ),
                ),
                ("date", models.DateField()),
            ],
        ),
    ]