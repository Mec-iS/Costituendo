import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def start(request):
    return render_to_response('home/start.html')