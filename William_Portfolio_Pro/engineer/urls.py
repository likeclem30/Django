from django.urls import path
from engineer import views

urlpatterns = [
    path('', views.engineer, name='engineer'),
    path('resume/', views.resume, name='resume'),
]