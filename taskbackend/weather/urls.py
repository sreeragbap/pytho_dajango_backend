from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('get_weather_info/', views.get_weather_info, name='get_weather_info'),
    path('get_citycodes/',views.get_citycodes,name='get_citycodes')
]