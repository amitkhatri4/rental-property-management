# Generated by Django 4.0.3 on 2024-02-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='map',
        ),
        migrations.AddField(
            model_name='property',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
