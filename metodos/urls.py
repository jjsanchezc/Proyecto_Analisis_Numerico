from django.contrib import admin
from django.urls import path
from metodos import views


urlpatterns = [
path('', views.home, name="home"),
path('metodosLineal', views.metodosLineal, name="metodosLineal"),
path('ecuaciones', views.ecuaciones, name="ecuaciones"),
path('biseccion/',views.bisec, name="biseccion"),
path('busquedas-incrementales/',views.busIncr, name="busquedas-incrementales"),
path('newton/', views.newton, name="newton"),
path('calcular/',views.calcular, name= "calcular"),

]
