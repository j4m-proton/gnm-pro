from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import OfficeLocation,ContactInfo,ContactUs

def contact(request):
    office_locations = OfficeLocation.objects.all()
    contactsection = ContactInfo.objects.get()
    hqOffice = OfficeLocation.objects.filter(isHQ=True)
    
    
    context = {
        'hqOffice': hqOffice,
        'office_locations': office_locations,
        'contactsection': contactsection
    }
    return render(request, "contact-us/contact-us.html",context)

def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        full_name=full_name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )

    

    data = {
        "bool": True,
        "message": "Message Sent Successfully"
    }

    return JsonResponse({"data":data})