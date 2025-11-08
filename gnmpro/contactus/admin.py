from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSocialHandle, OfficeLocation, SiteSupportContact,ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'opening_hours')
    search_fields = ('title',)

# ============================
# 🌐 Site Social Handles
# ============================
@admin.register(SiteSocialHandle)
class SiteSocialHandleAdmin(admin.ModelAdmin):
    list_display = ("platform", "url_link", "icon_preview", "is_active")
    list_editable = ("is_active",)
    search_fields = ("platform", "url")
    list_filter = ("platform", "is_active")
    readonly_fields = ("icon_preview",)

    fieldsets = (
        ("🔗 Social Media Info", {
            "fields": ("platform", "url", "is_active", "icon_preview")
        }),
    )

    def url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    url_link.short_description = "Social Link"

    def icon_preview(self, obj):
        icon = obj.get_icon_path()
        return format_html(
            '<img src="/static/{}" width="25" height="25" style="border-radius:3px;">', icon
        )
    icon_preview.short_description = "Icon"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, f"✅ {obj.platform.capitalize()} handle saved successfully!")


# ============================
# 🏢 Office Locations
# ============================
@admin.register(OfficeLocation)
class OfficeLocationAdmin(admin.ModelAdmin):
    list_display = ("location_type", "address", "city", "country", "phone", "email", "map_preview")
    search_fields = ("address", "city", "country", "email")
    list_filter = ("location_type", "country")
    readonly_fields = ("map_preview",)

    fieldsets = (
        ("🏠 Basic Information", {
            "fields": ("location_type", "address", "city", "postal_code", "country")
        }),
        ("📞 Contact Info", {
            "fields": ("phone", "email")
        }),
        ("🗺️ Map Info", {
            "fields": ("latitude", "longitude", "map_link", "map_preview")
        }),
    )

    def map_preview(self, obj):
        if obj.map_link:
            return format_html('<a href="{}" target="_blank">🌍 Open Map</a>', obj.map_link)
        return "No map link"
    map_preview.short_description = "Map Link"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, "📍 Office location saved successfully!")


# ============================
# 💬 Site Support Contacts
# ============================
@admin.register(SiteSupportContact)
class SiteSupportContactAdmin(admin.ModelAdmin):
    list_display = ("contact_name", "normal_call", "whatsapp", "email", "telegram")
    search_fields = ("contact_name", "email", "normal_call")
    list_filter = ("email",)
    fieldsets = (
        ("👤 Contact Info", {
            "fields": ("contact_name", "email", "normal_call", "whatsapp", "telegram")
        }),
        ("🌐 Social Links", {
            "fields": ("facebook", "twitter", "instagram", "linkedin")
        }),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, f"💡 Support contact '{obj.contact_name or 'Unnamed'}' saved successfully!")

