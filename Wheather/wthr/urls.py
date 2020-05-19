from wthr import views
from django.urls import path

urlpatterns = [
    path('', views.weather, name= 'weather'),
    
]