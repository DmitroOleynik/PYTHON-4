# Generated by Django 5.2.3 on 2025-07-04 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_musician_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musician',
        ),
        migrations.AddField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.musician'),
        ),
    ]
