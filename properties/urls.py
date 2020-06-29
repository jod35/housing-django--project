from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'properties'

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('agents', views.agents, name='agents'),
    path('admin-login-only', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='admin_login'),
    path('admin-logout', auth_views.LogoutView.as_view(), name='admin_logout'),
]
