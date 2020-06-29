from django.shortcuts import render
from .models import House, WareHouse, Land
from django.contrib import messages
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
    houses = House.objects.all()
    warehouses = WareHouse.objects.all()
    land = Land.objects.all()
    agents = User.objects.all()
    context = {
        'houses': houses,
        'warehouses': warehouses,
        'land_plots': land,
        'agents': agents
    }
    return render(request, 'properties/home.html', context)


@login_required
def create_house(request):
    context = {}
    return render(request, 'properties/createhouse.html', context)


@login_required
def create_warehouse(request):
    context = {}
    return render(request, 'properties/createwarehouse.html', context)


@login_required
def create_land_plot(request):
    context = {}
    return render(request, 'properties/createplot.html', context)


@login_required
def change_house(request):
    context = {}
    return render(request, 'properties/changehouse.html', context)


@login_required
def create_agent(request):
    context = {}
    return render(request, 'properties/addagent.html', context)


@login_required
def change_warehouse(request):
    context = {}
    return render(request, 'properties/changewarehouse.html', context)


@login_required
def change_plot(request):
    context = {}
    return render(request, 'properties/changeplot.html', context)
