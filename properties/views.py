from django.shortcuts import render
from .models import House, WareHouse, Land


def index(request):
    return render(request, 'properties/index.html')


def contacts(request):
    return render(request, 'properties/contacts.html')


def agents(request):
    return render(request, 'properties/agents.html')


def admin_dashboard(request):
    return render(request, 'properties/dashboard.html')
