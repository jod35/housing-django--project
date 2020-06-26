
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('properties.urls'),name='properties'),
    path('admin/', admin.site.urls),
]
