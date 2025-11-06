from django.contrib import admin
from .models import HeadTeam, MidleTopTeam, TeamMember


@admin.register(HeadTeam)
class HeadTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "email", "phone")
    list_editable = ("order",)
    search_fields = ("name", "role", "email", "phone")
    ordering = ("order",)
    fieldsets = (
        (None, {
            "fields": ("name", "role", "bio", "photo", "order")
        }),
        ("Contact Info", {
            "fields": ("email", "phone")
        }),
        ("Social Links", {
            "fields": ("linkedin", "twitter", "instagram", "facebook")
        }),
    )


@admin.register(MidleTopTeam)
class MidleTopTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "email", "phone")
    list_editable = ("order",)
    search_fields = ("name", "role", "email", "phone")
    ordering = ("order",)
    fieldsets = (
        (None, {
            "fields": ("name", "role", "bio", "photo", "order")
        }),
        ("Contact Info", {
            "fields": ("email", "phone")
        }),
        ("Social Links", {
            "fields": ("linkedin", "twitter", "instagram", "facebook")
        }),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "email", "phone")
    list_editable = ("order",)
    search_fields = ("name", "role", "email", "phone")
    ordering = ("order",)
    fieldsets = (
        (None, {
            "fields": ("name", "role", "bio", "photo", "order")
        }),
        ("Contact Info", {
            "fields": ("email", "phone")
        }),
        ("Social Links", {
            "fields": ("linkedin", "twitter", "instagram", "facebook")
        }),
    )

