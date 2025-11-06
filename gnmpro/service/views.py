from django.shortcuts import render,get_object_or_404
from .models import ServicesSection,Service, HardworkingSection,TestimonialSectionContent
from home.models import Testimonial

def service(request):
    section = ServicesSection.objects.first()
    hardworking = HardworkingSection.objects.prefetch_related('features').first()
    # Tuchukue content ya upande wa kushoto
    left_content = TestimonialSectionContent.objects.first()  # assuming kuna only one entry

    # Tuchukue testimonials zote kushoto ku-display kwenye swiper
    testimonials = Testimonial.objects.all()
    
    context = {
        'servicetop': section,
        'hardworking': hardworking,
        "services": Service.objects.all(),
        "testimonial_content": left_content,
        "testimonials": testimonials,
    }
    return render(request, "service/our-services.html",context)

def service_detail_view(request, serviceId):
    service = get_object_or_404(Service, id=serviceId)
    details = service.details.prefetch_related(
        "sections__medias"
    ).all()
    return render(request, "service/service-detail.html", {
        "service": service,
        "details": details,
        "primary_color": "#FF6B00",  # replace with your actual primary color
        "secondary_color": "#FFD500", # replace with your actual secondary color
    })
