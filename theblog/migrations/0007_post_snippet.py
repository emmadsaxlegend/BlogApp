# Generated by Django 4.1.3 on 2022-11-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="Click Link above to read blog post", max_length=255
            ),
        ),
    ]
