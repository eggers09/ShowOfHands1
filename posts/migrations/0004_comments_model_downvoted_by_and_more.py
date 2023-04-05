# Generated by Django 4.1.6 on 2023-04-02 17:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0003_comments_model_reported_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments_model",
            name="downvoted_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="downvoted_comment_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comments_model",
            name="upvoted_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="upvoted_comment_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comments_model",
            name="vote_count",
            field=models.IntegerField(default=0),
        ),
    ]
