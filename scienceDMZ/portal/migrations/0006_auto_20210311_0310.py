# Generated by Django 3.1.6 on 2021-03-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20210311_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='access_key',
            field=models.CharField(max_length=1000, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ip_address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='port',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='secret_key',
            field=models.CharField(max_length=1000, null=True, unique=True),
        ),
    ]
