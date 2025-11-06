from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ('small_title', 'main_title')
    search_fields = ('small_title', 'main_title')


# ------------------------ INLINE CLASSES ------------------------

class ServiceDetailMediaInline(admin.TabularInline):
    model = ServiceDetailMedia
    extra = 1
    fields = ("preview", "image", "video", "video_url", "caption", "order")
    readonly_fields = ("preview",)
    ordering = ("order",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" style="border-radius:6px"/>', obj.image.url)
        elif obj.video:
            return format_html('<span style="color:green;">🎬 Video File</span>')
        elif obj.video_url:
            return format_html('<a href="{}" target="_blank">🌐 Video Link</a>', obj.video_url)
        return "-"
    preview.short_description = "Preview"


class ServiceDetailSectionInline(admin.StackedInline):
    model = ServiceDetailSection
    extra = 1
    fields = ("heading", "content", "order")
    ordering = ("order",)


# ------------------------ MAIN ADMINS ------------------------

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "order", "happy_client", "complete_shipment", "customer_reviews")
    list_editable = ("order",)
    search_fields = ("name", "description")
    ordering = ("order",)
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        ("Basic Info", {"fields": ("name", "slug", "description", "order")}),
        ("Stats", {"fields": ("happy_client", "complete_shipment", "customer_reviews")}),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "icon_preview", "excerpt")
    list_filter = ("category",)
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("icon_preview",)
    ordering = ("title",)
    fieldsets = (
        ("General Info", {"fields": ("title", "slug", "category", "excerpt", "content")}),
        ("Media & Icon", {"fields": ("icon_class", "icon_preview", "image", "brochure")}),
    )

    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html(f'<i class="fa {obj.icon_class}" style="font-size:20px;color:#0d6efd;"></i>')
        return "-"
    icon_preview.short_description = "Icon"


@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ("title", "service", "short_description", "created_at")
    search_fields = ("title", "short_description", "service__title")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("service", "id")
    inlines = [ServiceDetailSectionInline]

    fieldsets = (
        ("Basic Info", {"fields": ("service", "title", "slug", "short_description")}),
    )


@admin.register(ServiceDetailSection)
class ServiceDetailSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "service_detail", "order")
    list_editable = ("order",)
    search_fields = ("heading", "service_detail__title")
    ordering = ("service_detail", "order")
    inlines = [ServiceDetailMediaInline]


@admin.register(ServiceDetailMedia)
class ServiceDetailMediaAdmin(admin.ModelAdmin):
    list_display = ("section", "caption", "media_preview", "order")
    list_editable = ("order",)
    search_fields = ("caption", "section__heading")
    ordering = ("section", "order")
    readonly_fields = ("media_preview",)

    def media_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" style="border-radius:6px"/>', obj.image.url)
        elif obj.video:
            return format_html('<span style="color:green;">🎬 Video File</span>')
        elif obj.video_url:
            return format_html('<a href="{}" target="_blank">🌐 Video Link</a>', obj.video_url)
        return "-"
    media_preview.short_description = "Preview"


class HardworkingFeatureInline(admin.TabularInline):
    model = HardworkingFeature
    extra = 2  # number of blank feature rows to show
    fields = ('order', 'icon_class', 'title', 'description')
    ordering = ('order',)

@admin.register(HardworkingSection)
class HardworkingSectionAdmin(admin.ModelAdmin):
    list_display = ('small_title', 'main_title')
    inlines = [HardworkingFeatureInline]
    search_fields = ('small_title', 'main_title')
    
    
@admin.register(TestimonialSectionContent)
class TestimonialSectionContentAdmin(admin.ModelAdmin):
    list_display = ("main_title", "small_title")    