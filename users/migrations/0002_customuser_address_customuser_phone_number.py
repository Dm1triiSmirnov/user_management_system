# Generated by Django 4.2.4 on 2023-08-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
