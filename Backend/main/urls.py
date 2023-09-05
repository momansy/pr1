from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about_me, name='hire-me'),
    path('cv/', views.cv, name='cv'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.Sample, name='project'),
]