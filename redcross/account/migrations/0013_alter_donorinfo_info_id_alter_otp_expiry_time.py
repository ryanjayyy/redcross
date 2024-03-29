# Generated by Django 4.1.7 on 2023-05-14 03:47

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_donorinfo_info_id_alter_otp_expiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='info_id',
            field=models.CharField(default=account.models.generate_id, editable=False, max_length=7, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expiry_time',
            field=models.DateTimeField(),
        ),
    ]
