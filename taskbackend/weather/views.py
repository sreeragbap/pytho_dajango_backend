from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import WeatherInfo, CityInfo
from django.views.decorators.csrf import csrf_exempt


def get_citycodes(request):
    if request.method == "GET":
        weatherdetails = list(WeatherInfo.objects.values())
        citycodelist = []
        for single in weatherdetails:
            print(single)
            citycodelist.append(single['city_code'])
        return JsonResponse({"data": citycodelist})


def get_weather_info(request):
    if request.method == "GET":
        citycode=request.GET.get('data')
        print("=================")
        weatherdetails = list(WeatherInfo.objects.values())
        cityinfo = CityInfo.objects.all()
        print(cityinfo)
       
        print('======================================================')
        for weather in weatherdetails:
            for city in cityinfo:
                if citycode==weather['city_code'] and citycode == city.city_code.city_code:
                    print(type(city.city_name))
                    res = {'city_code': weather['city_code'],
                        'city_name': city.city_name,
                        'country_name': city.country_name,
                        'temperature':weather['temperature'],
                        'humidity':weather['humidity']}
            # weatherdetailslist.append(res)     
        print(weather['city_code'])  
        # print(city['city_code_id'])
        print("=============================")
        # print(citycodes)
        print("=============================")
        # weatherdetailslist = json.loads(json.dumps(weatherdetailslist, default=str))
        return JsonResponse(res)
