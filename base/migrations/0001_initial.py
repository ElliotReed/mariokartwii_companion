# Generated by Django 4.0.4 on 2022-06-14 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterBonus',
            fields=[
                ('label', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('acceleration', models.IntegerField(blank=True, null=True)),
                ('handling', models.IntegerField(blank=True, null=True)),
                ('drift', models.IntegerField(blank=True, null=True)),
                ('offroad', models.IntegerField(blank=True, null=True)),
                ('miniturbo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'character bonus',
            },
        ),
        migrations.CreateModel(
            name='CTGPTrack',
            fields=[
                ('label', models.CharField(max_length=75, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='EngineClass',
            fields=[
                ('label', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'engine classes',
            },
        ),
        migrations.CreateModel(
            name='GameMode',
            fields=[
                ('label', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleStat',
            fields=[
                ('label', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('acceleration', models.IntegerField(blank=True, null=True)),
                ('handling', models.IntegerField(blank=True, null=True)),
                ('drift', models.IntegerField(blank=True, null=True)),
                ('offroad', models.IntegerField(blank=True, null=True)),
                ('miniturbo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WiiTrack',
            fields=[
                ('label', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='WiiCup',
            fields=[
                ('label', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('image', models.CharField(blank=True, default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tracks', models.ManyToManyField(to='base.wiitrack')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('label', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('vehicle_class', models.CharField(blank=True, max_length=10, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=5, null=True)),
                ('image', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.vehiclestat')),
            ],
            options={
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='CTGPCup',
            fields=[
                ('label', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('image', models.CharField(blank=True, default='', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('default_tracks', models.ManyToManyField(to='base.ctgptrack')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('label', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('image', models.CharField(default='', max_length=25)),
                ('character_class', models.CharField(blank=True, max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bonus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.characterbonus')),
            ],
        ),
    ]
