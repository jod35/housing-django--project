from django.shortcuts import render, redirect
from .models import House, WareHouse, Land
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import HouseCreationForm, WareHouseCreateForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


def index(request):
    return render(request, 'properties/index.html')


def contacts(request):
    return render(request, 'properties/contacts.html')


def agents(request):
    return render(request, 'properties/agents.html')

# @login_required
# def houses(request):
#     houses=
#     return render(request,'properties/houses.html')


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
    form = HouseCreationForm()

    if request.method == 'POST':
        form = HouseCreationForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.agent = request.user

            obj.save()
            messages.success(request, 'Item added successfully')

            return redirect('properties:houses')
    context = {
        'form': form
    }
    return render(request, 'properties/createhouse.html', context)


class HouseListView(ListView):
    queryset = House.objects.order_by('-id').all()
    context_object_name = 'houses'
    template_name = 'properties/houses.html'
    paginate_by = 20


class HouseUpdateView(UpdateView):
    model = House
    fields = ['name', 'location', 'price', 'bedrooms', 'bathrooms']

    template_name = "properties/houseupdate.html"
    success_url = '/houses/'


def delete_house(request, id):
    house = House.objects.get(id=id)

    if request.method == 'POST':
        house.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('properties:houses')
    context = {
        'house': house
    }
    return render(request, 'properties/housedelete.html', context)


# @login_required
class WareHouseListView(ListView):
    queryset = WareHouse.objects.order_by('-id').all()
    template_name = 'properties/warehouses.html'
    paginate_by = 20
    context_object_name='warehouses'


class WareHouseUpdateView(UpdateView):
    model=WareHouse
    template_name='properties/warehouseupdate.html'
    success_url='/warehouses/'
    fields=['name','location','price','space']

def delete_warehouse(request, id):
    warehouse = WareHouse.objects.get(id=id)

    if request.method == 'POST':
        warehouse.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('properties:warehouses')
    context = {
        'house': warehouse
    }
    return render(request, 'properties/warehousedelete.html', context)


@ login_required
def create_warehouse(request):
    form = WareHouseCreateForm()

    if request.method == 'POST':
        form=WareHouseCreateForm(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)

            obj.agent=request.user

            obj.save()

            messages.success(request,'Warehouse added Successfully')

            return redirect('properties:warehouses')
    context = {'form': form}
    return render(request, 'properties/createwarehouse.html', context)


@ login_required
def create_land_plot(request):
    context = {}
    return render(request, 'properties/createplot.html', context)


@ login_required
def change_house(request):
    context = {}
    return render(request, 'properties/changehouse.html', context)


@ login_required
def create_agent(request):
    context = {}
    return render(request, 'properties/addagent.html', context)


@ login_required
def change_warehouse(request):
    context = {}
    return render(request, 'properties/changewarehouse.html', context)


@ login_required
def change_plot(request):
    context = {}
    return render(request, 'properties/changeplot.html', context)
