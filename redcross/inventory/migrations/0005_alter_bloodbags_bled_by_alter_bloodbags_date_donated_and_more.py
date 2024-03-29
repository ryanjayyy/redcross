# Generated by Django 4.1.7 on 2023-04-30 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_donorinfo_occupation'),
        ('inventory', '0004_alter_bloodbags_date_donated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbags',
            name='bled_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bloodbags',
            name='date_donated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bloodbags',
            name='info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.donorinfo'),
        ),
        migrations.AlterField(
            model_name='bloodbags',
            name='serial_no',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
