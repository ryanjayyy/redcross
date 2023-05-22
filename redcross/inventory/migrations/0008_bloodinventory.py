# Generated by Django 4.1.7 on 2023-05-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_bloodbags_date_donated'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodInventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('exp_date', models.DateTimeField()),
                ('qty', models.IntegerField()),
                ('bag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.bloodbags')),
            ],
        ),
    ]
