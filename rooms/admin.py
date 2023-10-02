from django.contrib import admin
from .models import Room, RoomImage


class RoomAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "posted_by")


class RoomImageAdmin(admin.ModelAdmin):
    list_display = ("room", "image")


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage, RoomImageAdmin)
