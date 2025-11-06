from django.shortcuts import render
from .models import AboutSection,AboutExperienceSection,ProfessionalismSection
from team.models import HeadTeam


def about(request):
    about_sections = AboutSection.objects.prefetch_related('features').all()
    sections = AboutExperienceSection.objects.prefetch_related('features', 'testimonial').all()
    professionalism = ProfessionalismSection.objects.prefetch_related('skills').all()
    headTeam = HeadTeam.objects.all()
    context = {
        'about_sections': about_sections,
        'sections': sections,
        'professionalism':professionalism,
        'headTeam':headTeam
    }
    return render(request, "about-us/about.html",context)
