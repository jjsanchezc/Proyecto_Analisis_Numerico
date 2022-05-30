from django.contrib import admin
from django.urls import path
from metodos import views


urlpatterns = [
path('', views.home, name="home"),
path('metodosNoLineal', views.metodosNoLineal, name="metodosNoLineal"),
path('sistemaDeEcua', views.sistemaDeEcua, name="sistemaDeEcua"),
path('biseccion/',views.bisec, name="biseccion"),
path('busquedas-incrementales/',views.busIncr, name="busquedas-incrementales"),
path('newton/', views.newton, name="newton"),
path('calcular/',views.calcular, name= "calcular"),
path('puntoFijo/',views.puntoFijo, name= "puntoFijo"),
path('reglaFalsa/',views.reglaFalsa, name= "reglaFalsa"),
path('secante/',views.secante, name= "secante"),
path('raicesMult/',views.raicesMult, name= "raicesMult"),
]
