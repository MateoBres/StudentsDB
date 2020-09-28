"""Fichero URLs module."""
#Django
from django.contrib import admin
from django.urls import path
#Local




urlpatterns = [
    
    path('', admin.site.urls)
]
