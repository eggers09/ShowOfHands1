# Generated by Django 4.1.6 on 2023-05-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0014_alter_noti_model_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="noti_model",
            name="content_text",
            field=models.CharField(default="empty comment", max_length=500),
        ),
    ]