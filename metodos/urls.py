from django.contrib import admin
from django.urls import path
from metodos import views


urlpatterns = [
path('', views.home, name="home"),
path('biseccion/',views.bisec, name="biseccion"),
path('busquedas-incrementales/',views.busIncr, name="busquedas-incrementales"),
path('newton/', views.newton, name="newton"),
path('puntoFijo/',views.puntoFijo, name= "puntoFijo"),
path('reglaFalsa/',views.reglaFalsa, name= "reglaFalsa"),
path('secante/',views.secante, name= "secante"),
path('raicesMult/',views.raicesMult, name= "raicesMult"),
path('gauss/',views.gauss, name= "gauss"),
path('Jacobi/',views.jacobi, name= "jacobi"),
path('gaussSeidel/',views.gaussSeidel, name= "gaussSeidel"),
path('SOR/',views.SOR, name= "SOR"),
path('vandermonde/',views.vandermonde, name= "vandermonde"),
path('spline/',views.spline, name= "spline"),
path('newtonIn/',views.newtonIn, name= "newtonIn"),
]
