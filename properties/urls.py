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

    path('admin-logout', auth_views.LogoutView.as_view(
        template_name='properties/loggedout.html'), name='admin_logout'),

    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('createhouse/', views.create_house, name="create_house"),

    path('createwarehouse', views.create_warehouse, name='create_warehouse'),

    path('createplot', views.create_land_plot, name='create_land_plot'),

    path('register_agent', views.create_agent, name='create_agent'),

    path('houses/', views.HouseListView.as_view(), name='houses'),


    path('update_house/<pk>/', views.HouseUpdateView.as_view(), name='house_update'),

    path('delete_house/<int:id>', views.delete_house, name='house_delete'),

    path('warehouses/', views.WareHouseListView.as_view(), name='warehouses'),

    path('update_warehouse/<pk>/',views.WareHouseUpdateView.as_view(),name='warehouse_update'),

]
