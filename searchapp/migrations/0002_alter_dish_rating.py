# Generated by Django 5.0.7 on 2024-07-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("searchapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="rating",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
