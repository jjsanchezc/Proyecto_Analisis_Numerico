from django.contrib import admin
from django.urls import path
from metodos import views


urlpatterns = [
path('', views.home, name="home"),
path('metodosLineales/', views.metodosLineales, name="metodosLineales"),
path('ecuaciones/', views.ecuaciones, name="ecuaciones"),
path('metodosLineales/biseccion',views.bisec,name='biseccion'),
path('metodosLineales/biseccion/calcular',views.bisec,name='cbiseccion')


]
