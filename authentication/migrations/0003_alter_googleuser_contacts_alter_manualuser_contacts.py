# Generated by Django 4.1 on 2023-08-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0002_rename_email_contact_contact_email"),
        ("authentication", "0002_googleuser_contacts_manualuser_contacts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="googleuser",
            name="contacts",
            field=models.ManyToManyField(blank=True, to="contact.contact"),
        ),
        migrations.AlterField(
            model_name="manualuser",
            name="contacts",
            field=models.ManyToManyField(blank=True, to="contact.contact"),
        ),
    ]
