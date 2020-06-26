from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class House(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    location=models.CharField(max_length=25)
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    toilets=models.IntegerField()    
    swimming_pool=models.BooleanField()
    agent=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class WareHouse(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=25)
    price=models.IntegerField()
    space=models.DecimalField(max_digits=11,decimal_places=3)
    agent=models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name



class Land(models.Model):
    # LAND_TYPES=(
    #     ('mailo','Mailo'),
    #     ('')
    # )
    location=models.CharField(max_length=25)
    space=models.DecimalField(max_digits=11,decimal_places=3)
    price=models.IntegerField()

    agent=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agent}'s land"