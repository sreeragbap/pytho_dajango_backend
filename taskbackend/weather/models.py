from django.db import models
from django.contrib import admin

class WeatherInfo(models.Model):
    city_code = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    
class CityInfo(models.Model):
    city_code = models.ForeignKey(WeatherInfo,on_delete=models.CASCADE,)
    city_name = models.CharField(max_length=20)
    country_name = models.CharField(max_length=20)
   