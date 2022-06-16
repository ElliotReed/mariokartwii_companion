from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from base.models import Character, Vehicle, WiiTrack, GameMode, EngineClass
from user.models import User


class WiiTrackTime(models.Model):
    time = models.DurationField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    track = models.ForeignKey(
        WiiTrack, on_delete=PROTECT, blank=True, null=True)
    character = models.ForeignKey(
        Character, on_delete=PROTECT, blank=True, null=True)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=PROTECT, blank=True, null=True)
    engine_class = models.ForeignKey(
        EngineClass, on_delete=PROTECT, blank=True, null=True)
    game_mode = models.ForeignKey(
        GameMode, on_delete=PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.track.label + ', ' + self.user.username
