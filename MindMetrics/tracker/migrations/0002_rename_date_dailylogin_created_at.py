# Generated by Django 5.1.4 on 2025-01-06 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailylogin',
            old_name='date',
            new_name='created_at',
        ),
    ]
