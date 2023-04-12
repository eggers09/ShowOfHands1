# Generated by Django 4.1.6 on 2023-04-05 13:56

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_post_model_reported_by_post_model_reported_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post_model",
            name="category",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("sports", "Sports"),
                    ("fantasy", "Fantasy"),
                    ("entertainment", "Entertainment"),
                    ("misc", "Misc"),
                ],
                default="misc",
                max_length=100,
            ),
        ),
    ]