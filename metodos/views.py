from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HTTPResponse("templates/home.html")