# Generated by Django 5.1.1 on 2024-10-11 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0003_fit_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fit',
            name='user',
        ),
    ]
