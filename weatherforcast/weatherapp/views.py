from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
import random
import datetime
import requests
import json

# Create your views here.


def index(request):
    today = datetime.datetime.now()
    date = today.strftime("%B %d, %Y")
    time = today.strftime("%H:%M:%S")
    cities = ['New York', 'Lagos', 'Accra', 'Abuja', 'Alabama', 'London', 'Wales', 'Agra', 'Beijing', 'Berlin',
              'Bogota', 'Cairo', 'Chicago', 'Giza']
    city = random.choices(cities)[0]
    API_Key = "5ff23556993787d0a9b98bbf4df60dfb"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"
    response = requests.get(url)
    res = response.json()
    if res["cod"] != "404":
        visibility = res["visibility"]
        data = res["main"]
        # Storing the live temperature data
        live_temperature = data["temp"]
        live_humidity = data["humidity"]
        # Storing the live pressure data
        live_pressure = data["pressure"]
        desc = res["weather"]
        weather_condition = desc[0]["main"]
        weather_description = desc[0]["description"]
        print("Temperature (in Kelvin scale): " + str(live_temperature))
        print("Pressure: " + str(live_pressure))
        print("Description: " + str(weather_description))
        city_found = True
    else:
        city_found = False
        live_temperature = 0
        live_humidity = None
        live_pressure = None
        weather_condition = None
        weather_description = None
        visibility = None
        print("Please enter a valid city name")

    return render(request, "index.html", {"temperature": int(live_temperature), "humidity": live_humidity,
                                          "pressure": live_pressure, "city_found": city_found,
                                          "weather_condition": weather_condition, "weather_description":
                                              weather_description, "visibility": visibility, "day": time, "date": date,
                                          "city": city})


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['name']
        lastname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['repeatpassword']
        if password == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Email Already In Use')
                return redirect('/signup')

            elif firstname == "":
                messages.info(request, 'Name can not be empty')
                return redirect('/signup')

            elif lastname == "":
                messages.info(request, 'Name can not be empty')
                return redirect('/signup')

            elif email == "":
                messages.info(request, 'Email name can not be empty')
                return redirect('/signup')

            elif len(password) < 8:
                messages.info(request, 'password is too short. Try again')
                return redirect('/signup')

            else:
                user = User.objects.create_user(username=email, email=firstname, password=password,
                                                first_name=firstname, last_name=lastname)
                user.save()
                l_user = auth.authenticate(username=email, password=password)
                auth.login(request, l_user)
                request.session['userId'] = email
                return redirect('/home')
        else:
            messages.info(request, 'passwords does not match')
            return redirect('/signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['userId'] = email
            return redirect('/home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('/login')
    else:
        return render(request, 'login.html')


def home(request):
    if not request.session.get('userId', None):
        return redirect("/login")
    else:
        pass
    today = datetime.datetime.now()
    date = today.strftime("%B %d, %Y")
    time = today.strftime("%H:%M:%S")
    if request.method == "POST":
        city = request.POST['city']
    else:
        cities = ['New York', 'Lagos', 'Accra', 'Abuja', 'Alabama', 'London', 'Wales', 'Agra', 'Beijing', 'Berlin',
                  'Bogota', 'Cairo', 'Chicago', 'Giza']
        city = random.choices(cities)[0]
    API_Key = "5ff23556993787d0a9b98bbf4df60dfb"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"
    response = requests.get(url)
    res = response.json()
    if res["cod"] != "404":
        visibility = res["visibility"]
        data = res["main"]
        # Storing the live temperature data
        live_temperature = data["temp"]
        live_humidity = data["humidity"]
        # Storing the live pressure data
        live_pressure = data["pressure"]
        desc = res["weather"]
        weather_condition = desc[0]["main"]
        weather_description = desc[0]["description"]
        print("Temperature (in Kelvin scale): " + str(live_temperature))
        print("Pressure: " + str(live_pressure))
        print("Description: " + str(weather_description))
        city_found = True
    else:
        city_found = False
        live_temperature = 0
        live_humidity = None
        live_pressure = None
        weather_condition = None
        weather_description = None
        visibility = None
        print("Please enter a valid city name")

    return render(request, "index.html", {"temperature": int(live_temperature), "humidity": live_humidity,
                                          "pressure": live_pressure, "city_found": city_found, 
                                          "weather_condition": weather_condition, "weather_description": 
                                              weather_description, "visibility": visibility, "day": time, "date": date, 
                                          "city": city})


def contact(request):
    return render(request, "contact.html")


def news(request):
    return render(request, "news.html")


def live_cameras(request):
    return render(request, "live-cameras.html")


def photos(request):
    return render(request, "photos.html")


def single(request):
    return render(request, "single.html")
