from django.contrib import admin
from .models import WeatherInfo,CityInfo
# Register your models here.
admin.site.register(WeatherInfo)
admin.site.register(CityInfo)