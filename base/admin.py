from django.contrib import admin
from .models import Character, CharacterBonus, Vehicle, VehicleStat, CTGPCup, CTGPTrack, WiiCup, WiiTrack, GameMode, EngineClass

admin.site.register(Character)
admin.site.register(CharacterBonus)
admin.site.register(Vehicle)
admin.site.register(VehicleStat)
admin.site.register(CTGPCup)
admin.site.register(CTGPTrack)
admin.site.register(WiiCup)
admin.site.register(GameMode)
admin.site.register(EngineClass)


class WiiTrackAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(WiiTrack, WiiTrackAdmin)
