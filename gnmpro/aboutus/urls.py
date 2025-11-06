from . import views
from django.urls import path

app_name = "aboutus"

urlpatterns = [
    path("about-us/", views.about, name="about-page"),
    
]