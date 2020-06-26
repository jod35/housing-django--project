from . import views

from django.urls import path

app_name='properties'

urlpatterns = [
    path('',views.index,name='home'),
    path('contacts',views.contacts,name='contacts'),
    path('agents',views.agents,name='agents')
]