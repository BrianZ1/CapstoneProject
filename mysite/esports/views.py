from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'esports/home.html')

def playerSearch(request):
    return render(request, 'esports/playersearch.html')

def playerResults(request):
    return render(request, 'esports/playerresults.html')

def eventSearch(request):
    return render(request, 'esports/eventsearch.html')

def eventResults(request):
    return render(request, 'esports/eventresults.html')

def contact(request):
    return render(request, 'esports/contact.html')