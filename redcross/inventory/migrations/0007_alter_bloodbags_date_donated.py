# Generated by Django 4.1.7 on 2023-04-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_bloodbags_bled_by_alter_bloodbags_info_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbags',
            name='date_donated',
            field=models.DateTimeField(),
        ),
    ]
