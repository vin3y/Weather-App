
from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request
from django.http import HttpResponse 


def index(request):
    return HttpResponse("Home page will come soon")
    
  
  
def weather(request): 
    if request.method == 'POST': 
        city = request.POST.get('city', False);
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ecce255ff1979e470b39c2b3d927448c').read()
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + ' k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "wthr/weather.html", data) 
