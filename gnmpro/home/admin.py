from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("headline", "cta_text", "order")
   



# ============================
# 🌟 About Feature
# ============================
@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_preview", "short_description", "background_preview" ,"order")
    list_editable = ("order",)
    search_fields = ("title", "description")
    ordering = ("order",)
    readonly_fields = ("icon_preview","background_preview",)

    fieldsets = (
        ("💡 Feature Information", {
            "fields": ("icon_class", "icon_preview", "title", "description", "order"),
        }),
        
        ("🖼️ Background", {
            "fields": ("background_image", "background_preview")
        }),
    )
    
    def background_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" width="120" height="70" style="border-radius:6px;object-fit:cover;">', obj.background_image.url)
        return "No background image"
    background_preview.short_description = "Background Preview"

    def icon_preview(self, obj):
        return format_html('<i class="fa {} fa-lg"></i> &nbsp;({})', obj.icon_class, obj.icon_class)
    icon_preview.short_description = "Icon Preview"

    def short_description(self, obj):
        return (obj.description[:60] + "...") if len(obj.description) > 60 else obj.description
    short_description.short_description = "Description"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, f"✅ Feature '{obj.title}' saved successfully!")


# ============================
# 🏛️ About Section
# ============================
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "subheading", "button_text", "background_preview", "feature_count")
    search_fields = ("heading", "subheading", "description")
    readonly_fields = ("background_preview",)
    filter_horizontal = ("features",)

    fieldsets = (
        ("🧩 Section Info", {
            "fields": ("heading", "subheading", "description")
        }),
        ("🎯 Button", {
            "fields": ("button_text", "button_url")
        }),
        ("✨ Features", {
            "fields": ("features",)
        }),
        ("🖼️ Background", {
            "fields": ("background_image", "background_preview")
        }),
    )

    def background_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" width="120" height="70" style="border-radius:6px;object-fit:cover;">', obj.background_image.url)
        return "No background image"
    background_preview.short_description = "Background Preview"

    def feature_count(self, obj):
        return obj.features.count()
    feature_count.short_description = "Features Count"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, f"🎉 About section '{obj.heading}' saved successfully!")
        
        
        
    


class FactItemInline(admin.TabularInline):
    model = FactItem
    extra = 1
    fields = ("icon_preview", "icon_class", "number", "label", "order")
    readonly_fields = ("icon_preview",)
    ordering = ("order",)

    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html(f'<i class="fa {obj.icon_class}" style="font-size:18px; color:#007bff;"></i>')
        return "-"
    icon_preview.short_description = "Icon Preview"


@admin.register(FactSection)
class FactSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "call_text", "overlay_color", "fact_count")
    search_fields = ("heading", "subheading", "call_text")
    list_filter = ("overlay_color",)
    inlines = [FactItemInline]

    fieldsets = (
        (None, {
            "fields": ("heading", "subheading", "call_text", "overlay_color")
        }),
    )

    def fact_count(self, obj):
        return obj.facts.count()
    fact_count.short_description = "Total Facts"


@admin.register(FactItem)
class FactItemAdmin(admin.ModelAdmin):
    list_display = ("label", "section", "number", "order", "icon_preview")
    list_editable = ("order",)
    search_fields = ("label", "section__heading")
    list_filter = ("section",)
    ordering = ("section", "order")
    readonly_fields = ("icon_preview",)

    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html(f'<i class="fa {obj.icon_class}" style="font-size:18px; color:#28a745;"></i>')
        return "-"
    icon_preview.short_description = "Icon Preview"
        
        
        
class HomeFeatureInline(admin.TabularInline):
    model = HomeFeature
    extra = 1
    fields = ('title', 'description', 'icon', 'order')
    ordering = ('order',)


@admin.register(HomeFeatureSection)
class HomeFeatureSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading', 'video_url')
    inlines = [HomeFeatureInline]
    search_fields = ('heading', 'subheading')
    list_filter = ('heading',)


@admin.register(HomeFeature)
class HomeFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order')
    list_filter = ('section',)
    search_fields = ('title', 'description')
    ordering = ('order',)       
    
    
class WhyChooseUsFeatureInline(admin.TabularInline):
    model = WhyChooseUsFeature
    extra = 1
    fields = ('icon_class', 'title', 'description')
    show_change_link = True


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle', 'description')
    inlines = [WhyChooseUsFeatureInline]
    fieldsets = (
        ('Section Details', {
            'fields': ('title', 'subtitle', 'description', 'image'),
        }),
    )


@admin.register(WhyChooseUsFeature)
class WhyChooseUsFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'icon_class')
    search_fields = ('title', 'description', 'icon_class')
    list_filter = ('section',)    
    
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "url")
    list_editable = ("order",)
    search_fields = ("name",)
    ordering = ("order",)


@admin.register(QuoteSection)
class QuoteSectionAdmin(admin.ModelAdmin):
    list_display = ("heading_top", "heading_main", "call_text")
    search_fields = ("heading_main",)
    fieldsets = (
        ("Headings", {
            "fields": ("heading_top", "heading_main", "description")
        }),
        ("Call Info", {
            "fields": ("call_text",)
        }),
        ("Background", {
            "fields": ("background_image",)
        }),
    )


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "service", "created")
    list_filter = ("service", "created")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created",)
    ordering = ("-created",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "role", "rating", "order")
    list_editable = ("order",)
    search_fields = ("name", "company", "role")
    ordering = ("order",)    