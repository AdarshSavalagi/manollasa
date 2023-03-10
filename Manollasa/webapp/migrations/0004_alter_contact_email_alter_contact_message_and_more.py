# Generated by Django 4.1.4 on 2023-02-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0003_alter_contact_email_alter_contact_message_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="Email",
            field=models.CharField(default="nothing", max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="Message",
            field=models.TextField(default="nothing"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="Name",
            field=models.CharField(default="nothing", max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="Subject",
            field=models.TextField(default="nothing"),
        ),
        migrations.AlterField(
            model_name="register",
            name="Branch",
            field=models.CharField(
                blank=True,
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
                default="nothing",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="register",
            name="Email",
            field=models.CharField(default="nothing", max_length=100),
        ),
        migrations.AlterField(
            model_name="register",
            name="Name",
            field=models.CharField(blank=True, default="nothing", max_length=100),
        ),
        migrations.AlterField(
            model_name="register",
            name="Phone",
            field=models.CharField(blank=True, default="nothing", max_length=100),
        ),
        migrations.AlterField(
            model_name="register",
            name="Place",
            field=models.CharField(blank=True, default="nothing", max_length=100),
        ),
    ]
