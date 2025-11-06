from django.contrib import admin
from django.utils.html import format_html
from .models import SiteMainSettings, SiteTheme

# ============================
# Site Main Settings Admin
# ============================
@admin.register(SiteMainSettings)
class SiteMainSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "main_email", "main_contact", "show_logo", "working_hours")
    search_fields = ("site_name", "main_email", "main_contact")
    list_filter = ("main_email",)
    readonly_fields = ("show_logo",)

    fieldsets = (
        ("🏠 Basic Info", {
            "fields": ("site_name", "another_name", "slogan", "logo", "show_logo")
        }),
        ("📞 Contact Details", {
            "fields": ("main_contact", "main_email", "main_location", "working_hours")
        }),
    )

    def show_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80" height="80" style="border-radius:5px;" />', obj.logo.url)
        return "No Logo"
    show_logo.short_description = "Preview Logo"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, "✅ Site settings saved successfully!")


# ============================
# Site Theme Admin
# ============================
@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ("name", "primarycolor", "secondarycolor", "is_default_theme", "colored_preview")
    list_editable = ("is_default_theme",)
    search_fields = ("name",)
    list_filter = ("is_default_theme",)
    readonly_fields = ("colored_preview",)

    fieldsets = (
        ("🎨 Theme Info", {
            "fields": ("name", "primarycolor", "secondarycolor", "is_default_theme", "colored_preview")
        }),
    )

    def colored_preview(self, obj):
        return format_html(
            '<div style="display:flex;align-items:center;gap:8px;">'
            '<div style="width:40px;height:20px;background:{};border:1px solid #ccc;"></div>'
            '<div style="width:40px;height:20px;background:{};border:1px solid #ccc;"></div>'
            '</div>', obj.primarycolor, obj.secondarycolor
        )
    colored_preview.short_description = "Color Preview"

    def save_model(self, request, obj, form, change):
        if obj.is_default_theme:
            SiteTheme.objects.exclude(pk=obj.pk).update(is_default_theme=False)
        super().save_model(request, obj, form, change)
        self.message_user(request, f"🎉 Theme '{obj.name}' updated successfully!")

