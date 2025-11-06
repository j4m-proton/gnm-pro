from django.shortcuts import render

def contact(request):
    return render(request, "contact-us/contact-us.html")
