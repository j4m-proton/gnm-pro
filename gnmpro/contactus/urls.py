from . import views
from django.urls import path

app_name = "contactus"

urlpatterns = [
    path("contact-us/", views.contact, name="contact-us"),
    
]