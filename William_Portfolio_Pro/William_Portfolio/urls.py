from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import projects.views


urlpatterns = [
    path("home/", projects.views.home,name='home'),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path('', include('engineer.urls')),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

