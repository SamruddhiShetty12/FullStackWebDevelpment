# Generated by Django 5.1.1 on 2024-10-16 13:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0004_remove_fit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='fit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
