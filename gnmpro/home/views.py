from django.shortcuts import render,redirect
from .models import HeroSlide, AboutSection,FactSection,Testimonial,HomeFeatureSection,HomeFeature,WhyChooseUs,QuoteSection,Quote
from service.models import Service, ServiceCategory
from team.models import MidleTopTeam




def home(request):
    PCslides = HeroSlide.objects.filter(isImageForPC=True)
    Phoneslides = HeroSlide.objects.filter(isImageForPC=False)
    about_section = AboutSection.objects.prefetch_related('features').first()
    fact_section = FactSection.objects.prefetch_related('facts').first()
    
    section = HomeFeatureSection.objects.first()
    features = HomeFeature.objects.order_by("order")
    whychooseus = WhyChooseUs.objects.prefetch_related("features").first()
    
    quote_section = QuoteSection.objects.first()
    clientReviews = Testimonial.objects.all()
    
    team_members = MidleTopTeam.objects.all()
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service_id = request.POST.get("service")
        notes = request.POST.get("notes")

    
        service = None
        if service_id:
            try:
                service = Service.objects.get(id=service_id)
            except Service.DoesNotExist:
                service = None

        # Save kwenye DB
        Quote.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            notes=notes
        )
        return redirect("home:quote_success") 
    
    context = {
        'PCslides':PCslides,
        'Phoneslides': Phoneslides,
        'clientReviews': clientReviews,
        "about_section": about_section,
        "fact_section": fact_section,
        "section": section,
        "whychooseus": whychooseus,
        "features": features,
        'team_members': team_members,
        'quote_section': quote_section,
        "service_categories": ServiceCategory.objects.all().order_by("order"),
        "services": Service.objects.filter()
    }
    return render(request, "home/index.html",context)

def quote_success(request):
    return render(request, "success/qoute-success.html")