from django.shortcuts import render
from .models import OfficeLocation,ContactInfo

def contact(request):
    office_locations = OfficeLocation.objects.all()
    contactsection = ContactInfo.objects.get()
    context = {
        'office_locations': office_locations,
        'contactsection': contactsection
    }
    return render(request, "contact-us/contact-us.html",context)
