# Generated by Django 3.2.8 on 2022-03-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0007_alter_request_is_ajax'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='query_params',
            field=models.JSONField(default={}, verbose_name='query_params'),
        ),
        migrations.AddField(
            model_name='request',
            name='post_body',
            field=models.JSONField(default={}, verbose_name='post_body'),
        ),
    ]
