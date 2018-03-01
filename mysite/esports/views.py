from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import PlayerSearchForm, EventSearchForm, ContactForm

import sys
sys.path.append(r'..\code')
import main

def home(request):
    request.session.flush()
    return render(request, 'esports/home.html')

def playerSearch(request):    
    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        
        if form.is_valid():
          request.session['player_name'] = form.cleaned_data['player_name']
          request.session['game'] = form.cleaned_data['game']
          request.session['num_bullet'] = form.cleaned_data['num_bullet']
          
          return HttpResponseRedirect('/esports/playersearch/' + request.session.get('player_name', None))
    else:
        form = PlayerSearchForm()

    return render(request, 'esports/playersearch.html', {'form': form})

def playerResults(request, name):
    try:
        player_name = request.session.get('player_name', None)
        game = request.session.get('game', None)
        num_bullet = request.session.get('num_bullet', None)

        summary = main.player_search(player_name, game, num_bullet)
    
        context = {'player_name': player_name, 'summary': summary}
    except:
        raise Http404("Player Not Found")
  
    return render(request, 'esports/playerresults.html', context)

def eventSearch(request):
    if request.method == 'POST':
        form = EventSearchForm(request.POST)
        
        if form.is_valid():
          request.session['event_name'] = form.cleaned_data['event_name']
          request.session['game'] = form.cleaned_data['game']
          
          return HttpResponseRedirect('/esports/eventsearch/' + request.session.get('event_name', None))
    else:
        form = EventSearchForm()
        
    return render(request, 'esports/eventsearch.html', {'form': form})

def eventResults(request, name):
    try:
        event_name = request.session.get('event_name', None)
        game = request.session.get('game', None)
        
        sorted_team_player_list = main.event_search(event_name, game)
        
        context = {'event_name': event_name, 'game': game, 'sorted_team_player_list': sorted_team_player_list}
    except:
        raise Http404("Event Not Found")
        
    return render(request, 'esports/eventresults.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
          request.session['contact_name'] = form.cleaned_data['contact_name']
          request.session['contact_email'] = form.cleaned_data['contact_email']
          request.session['content'] = form.cleaned_data['content']
          
          return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    
    return render(request, 'esports/contact.html', {'form': form})
