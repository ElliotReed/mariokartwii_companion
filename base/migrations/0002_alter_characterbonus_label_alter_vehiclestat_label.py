# Generated by Django 4.0.4 on 2022-06-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterbonus',
            name='label',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiclestat',
            name='label',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
