# Generated by Django 5.1.5 on 2025-01-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
