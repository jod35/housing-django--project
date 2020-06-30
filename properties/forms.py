from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import House, WareHouse, Land
from django.contrib.auth.models import User


class AgentCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class HouseCreationForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('name', 'price', 'location', 'bedrooms',
                  'bathrooms', 'toilets', 'swimming_pool')


class WareHouseCreateForm(forms.ModelForm):
    class Meta:
        model = WareHouse
        fields = ('name', 'location', 'price', 'space',)
