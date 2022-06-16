from django.contrib import admin
from .models import WiiTrackTime


class WiiTrackTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ['track', 'get_user']

    @admin.display(description='username')
    def get_user(self, obj):
        return obj.user

    @admin.display(description='label')
    def get_track(self, obj):
        return obj.track


admin.site.register(WiiTrackTime, WiiTrackTimeAdmin)

# Register your models here.
