from . import views
from django.urls import path

app_name = "contactus"

urlpatterns = [
    path("contact-us/", views.contact, name="contact-us"),
    path("contact-us-message/", views.ajax_contact_form, name="drop-us-msg"),
]