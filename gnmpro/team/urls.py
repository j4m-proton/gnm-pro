from . import views
from django.urls import path

app_name = "team"

urlpatterns = [
    path("our-team/", views.team, name="team-page"),
    
]