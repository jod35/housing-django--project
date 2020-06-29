from django.shortcuts import render
from .models import House, WareHouse, Land
from .models import House, WareHouse, Land
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'properties/index.html')


def contacts(request):
    return render(request, 'properties/contacts.html')


def agents(request):
    return render(request, 'properties/agents.html')


@login_required
def admin_dashboard(request):
    return render(request, 'properties/home.html')
