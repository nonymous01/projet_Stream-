# Generated by Django 5.0.2 on 2024-02-14 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_stream', '0005_alter_media_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='user',
        ),
    ]
