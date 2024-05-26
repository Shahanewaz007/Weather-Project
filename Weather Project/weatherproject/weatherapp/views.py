from django.shortcuts import render
import requests
import datetime
# Create your views here.

def index(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'dhaka'
    
    api_id = 'cdfa2711d4235a5ef4e4ab67aa504c60'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':api_id, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    lon = None
    lat = None
    if 'coord' in res:
        lon = res['coord']['lon']
        lat = res['coord']['lat']
    cnt = 1
    url2 = f'https://api.openweathermap.org/data/2.5/forecast'
    PARAMS2 = {'lat':lat, 'lon':lon, 'cnt':cnt, 'appid':api_id, 'units':'metric'}
    req2 = requests.get(url=url2, params=PARAMS2)
    data = req2.json()
    if 'weather' in res and res['weather']:
        description1 = res['weather'][0]['description']
        icon1 = res['weather'][0]['icon']
        temp1 = res['main']['temp']
        temp_min1 = res['main']['temp_min']
        temp_max1 = res['main']['temp_max']
        day1 = datetime.date.today()
    else:
        description1 = "Weather information not available"
        icon1 = ""
        temp1 = 0
        temp_min1 = 0
        temp_max1 = 0
        day1 = datetime.date.today()
        
    if 'list' in data and data['list'] and 'weather' in data['list'][0] and data['list'][0]['weather']:
        description2 = data['list'][0]['weather'][0]['description']
        icon2 = data['list'][0]['weather'][0]['icon']
        temp2 = data['list'][0]['main']['temp']
        temp_min2 = data['list'][0]['main']['temp_min']
        temp_max2 = data['list'][0]['main']['temp_max']
        day2 = datetime.date.today()
    else:
        description2 = "Weather information not available"
        icon2 = ""
        temp2 = 0
        temp_min2 = 0
        temp_max2 = 0
        day2 = datetime.date.today()
        
    today = {'description':description1, 'icon':icon1, 'temp':temp1, 'temp_min':temp_min1, 'temp_max':temp_max1, 'day':day1}
    tomorrow = {'description':description2, 'icon':icon2, 'temp':temp2, 'temp_min':temp_min2, 'temp_max':temp_max2, 'day':day2}
    
    return render(request, 'index.html', { 'today':today, 'tomorrow':tomorrow, 'city':city})


