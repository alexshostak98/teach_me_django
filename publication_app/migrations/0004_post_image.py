# Generated by Django 4.0 on 2022-01-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
