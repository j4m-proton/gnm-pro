
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home.urls")),
    path('admin/', admin.site.urls),
    path("app-about/", include("aboutus.urls")),
    path("app-service/", include("service.urls")),
    path("app-team/", include("team.urls")),
    path("app-contact/", include("contactus.urls")),
    path("app-blog/", include("blog.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)