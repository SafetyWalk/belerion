# Generated by Django 4.1 on 2023-08-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0001_initial"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="googleuser",
            name="contacts",
            field=models.ManyToManyField(to="contact.contact"),
        ),
        migrations.AddField(
            model_name="manualuser",
            name="contacts",
            field=models.ManyToManyField(to="contact.contact"),
        ),
    ]
