# Generated by Django 2.2.7 on 2020-06-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rece', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64),
        ),
    ]