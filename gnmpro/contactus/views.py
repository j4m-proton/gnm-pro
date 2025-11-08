from django.shortcuts import render,redirect
from .models import OfficeLocation,ContactInfo,ContactUs

def contact(request):
    office_locations = OfficeLocation.objects.all()
    contactsection = ContactInfo.objects.get()
    hqOffice = OfficeLocation.objects.filter(isHQ=True)
    
    if request.method == 'POST':
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
        
        return redirect("home:quote_success") 
    
    context = {
        'hqOffice': hqOffice,
        'office_locations': office_locations,
        'contactsection': contactsection
    }
    return render(request, "contact-us/contact-us.html",context)
