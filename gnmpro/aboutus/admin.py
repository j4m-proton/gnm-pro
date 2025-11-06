from django.contrib import admin
from .models import *


class AboutFeatureInline(admin.TabularInline):
    model = AboutFeature
    extra = 1
    fields = ('icon_class', 'title', 'description')
    verbose_name = "Feature"
    verbose_name_plural = "Features"


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    inlines = [AboutFeatureInline]


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'section')
    list_filter = ('section',)
    search_fields = ('title', 'description')


class AboutFeatureInline(admin.TabularInline):
    model = AboutFeatureItem
    extra = 1
    fields = ('icon_class', 'text')
    verbose_name = "Feature"
    verbose_name_plural = "Features"


@admin.register(AboutExperienceSection)
class AboutExperienceSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'small_title')
    search_fields = ('heading', 'description')
    inlines = [AboutFeatureInline]


@admin.register(AboutTestimonial)
class AboutTestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'section')
    search_fields = ('author', 'quote')



class ProfessionalSkillInline(admin.TabularInline):
    model = ProfessionalSkill
    extra = 1
    fields = ('skill_title', 'skill_value')
    verbose_name = "Skill"
    verbose_name_plural = "Skills"


@admin.register(ProfessionalismSection)
class ProfessionalismSectionAdmin(admin.ModelAdmin):
    list_display = ('small_title', 'heading')
    search_fields = ('small_title', 'heading', 'description')
    inlines = [ProfessionalSkillInline]