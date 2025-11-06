from . import views
from django.urls import path

app_name = "service"

urlpatterns = [
    path("we-provide/", views.service, name="service-page"),
    path("services/<int:serviceId>/details/", views.service_detail_view, name="Services-Details"),
    
]