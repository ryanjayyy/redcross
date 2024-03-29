# Generated by Django 4.1.7 on 2023-05-14 03:42

import account.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_donorinfo_info_id_alter_otp_expiry_time'),
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
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 3, 43, 24, 712866, tzinfo=datetime.timezone.utc)),
        ),
    ]
