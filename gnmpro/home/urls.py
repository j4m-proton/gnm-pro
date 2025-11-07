from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.home, name="home-page"),
    path("quote-success/", views.quote_success, name="quote_success"),
    
]