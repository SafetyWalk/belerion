# Generated by Django 4.1 on 2023-09-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("maps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coordinate",
            name="lat",
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name="coordinate",
            name="lng",
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
