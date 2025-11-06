from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("blog/", views.blogHome, name="blog-page"),
    path("blog-post/<int:blogId>/details/", views.blog_detail, name="blog-detail"),
    
]