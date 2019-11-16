from django.urls import path,include
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("blog", include("blog.urls")),
]