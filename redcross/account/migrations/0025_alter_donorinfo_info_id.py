# Generated by Django 4.1.7 on 2023-05-21 01:36

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_alter_donorinfo_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='info_id',
            field=models.CharField(default=account.models.generate_id, editable=False, max_length=7, primary_key=True, serialize=False, unique=True),
        ),
    ]
