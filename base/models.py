from django.db import models
from django.db.models.deletion import CASCADE


class CharacterBonus(models.Model):
    class Meta:
        verbose_name_plural = "character bonus"

    label = models.CharField(max_length=20, primary_key=True)
    total = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    acceleration = models.IntegerField(blank=True, null=True)
    handling = models.IntegerField(blank=True, null=True)
    drift = models.IntegerField(blank=True, null=True)
    offroad = models.IntegerField(blank=True, null=True)
    miniturbo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.label


class Character(models.Model):
    label = models.CharField(max_length=20, primary_key=True)
    image = models.CharField(max_length=25, default='')
    bonus = models.OneToOneField(
        CharacterBonus, on_delete=CASCADE)
    character_class = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class VehicleStat(models.Model):
    label = models.CharField(max_length=20, primary_key=True)
    total = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    acceleration = models.IntegerField(blank=True, null=True)
    handling = models.IntegerField(blank=True, null=True)
    drift = models.IntegerField(blank=True, null=True)
    offroad = models.IntegerField(blank=True, null=True)
    miniturbo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.label


class Vehicle(models.Model):
    class Meta:
        ordering = ['label']

    label = models.CharField(max_length=25, primary_key=True)
    stats = models.OneToOneField(VehicleStat, on_delete=CASCADE)
    vehicle_class = models.CharField(max_length=10, blank=True, null=True)
    vehicle_type = models.CharField(max_length=5, blank=True, null=True)
    image = models.CharField(default='', blank=True, null=True, max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class WiiTrack(models.Model):
    class Meta:
        ordering = ['order']

    label = models.CharField(max_length=50, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.label


class WiiCup(models.Model):
    label = models.CharField(max_length=50, unique=True, primary_key=True)
    image = models.CharField(max_length=50, blank=True, default='')
    tracks = models.ManyToManyField(WiiTrack)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class CTGPTrack(models.Model):
    class Meta:
        ordering = ['order']

    label = models.CharField(max_length=75, unique=True, primary_key=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.label


class CTGPCup(models.Model):
    label = models.CharField(max_length=50, unique=True, primary_key=True)
    image = models.CharField(max_length=50, blank=True, default='')
    default_tracks = models.ManyToManyField(CTGPTrack)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class GameMode(models.Model):
    label = models.CharField(max_length=15, blank=True, primary_key=True)

    def __str__(self):
        return self.label


class EngineClass(models.Model):
    class Meta:
        verbose_name_plural = "engine classes"

    label = models.CharField(max_length=15, blank=True, primary_key=True)

    def __str__(self):
        return self.label
