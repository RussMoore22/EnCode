# Generated by Django 4.2.7 on 2023-11-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("letterbox", "0004_encodedmessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="secretmessage",
            name="encrypted_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="EncodedMessage",
        ),
    ]
