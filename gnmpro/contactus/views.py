from django.shortcuts import render
from .models import OfficeLocation

def contact(request):
    office_locations = OfficeLocation.objects.all()
    context = {
        'office_locations': office_locations
    }
    return render(request, "contact-us/contact-us.html",context)
