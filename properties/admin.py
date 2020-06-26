from django.contrib import admin
from .models import WareHouse,House,Land


# Register your models here.

#House Admin
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display=('name','price','location','agent')
    list_filter=('uploaded','price','location')




#WareHouse Admin
@admin.register(WareHouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display=('name','location','space')
    list_filter=('location','space','uploaded')

#Land Admin
@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display=('location','space','agent')
    list_filter=('uploaded','space','location')

