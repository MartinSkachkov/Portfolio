from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.display_projects, name='projects'),
    path('contact/', views.contact, name='contact')
]