# Generated by Django 4.1.7 on 2023-05-21 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_expiredblood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodinventory',
            name='qty',
        ),
    ]
