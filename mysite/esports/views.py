from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.http import JsonResponse

from .forms import PlayerSearchForm, EventSearchForm, ContactForm
from .models import Comment, Player, Event

import sys
sys.path.append(r'..\code')
import main, articles, summarization

def home(request):
    request.session.flush()
    
    context = {
            'player_list': get_top_5_item_searches(Player),
            'event_list': get_top_5_item_searches(Event),
            }
    
    return render(request, 'esports/home.html', context)

def get_top_5_item_searches(database):
    return database.objects.order_by('-count')[:5]

def playerSearch(request):    
    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        
        if form.is_valid():
            request.session['player_name'] = form.cleaned_data['player_name']
            request.session['game'] = form.cleaned_data['game']
            request.session['num_bullet'] = form.cleaned_data['num_bullet']
  
            check_player = Player.objects.filter(name=form.cleaned_data['player_name'])
            
            if len(check_player) == 0:
                new_player = Player(name=form.cleaned_data['player_name'], count = 1)
                new_player.save()
            else:
                player = Player.objects.get(name=form.cleaned_data['player_name'])
                player.increment_count()
                player.save()
          
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
                      
            check_event = Event.objects.filter(name=form.cleaned_data['event_name'])
            
            if len(check_event) == 0:
                new_event = Event(name=form.cleaned_data['event_name'], count = 1)
                new_event.save()
            else:
                event = Event.objects.get(name=form.cleaned_data['event_name'])
                event.increment_count()
                event.save()
          
            return HttpResponseRedirect('/esports/eventsearch/' + request.session.get('event_name', None))
    else:
        form = EventSearchForm()
        
    return render(request, 'esports/eventsearch.html', {'form': form})

def eventResults(request, name):
    try:
        event_name = request.session.get('event_name', None)
        game = request.session.get('game', None)
        
        event_extractor = articles.EventSeperator(event_name, game)

        site = event_extractor.get_website();
        sorted_team_player_list, player_list = event_extractor.get_player_team_names(site)
              
        request.session['sorted_team_player_list'] = sorted_team_player_list
    
        context = {'event_name': event_name,
                   'game': game,
                   'sorted_team_player_list': sorted_team_player_list,
                   'team_name': next(iter(sorted_team_player_list)),
                   }
    except:
        raise Http404("Event Not Found")
        
    return render(request, 'esports/eventresults.html', context)

def eventResultsTeam(request, name, team):
    try:
        event_name = request.session.get('event_name', None)
        game = request.session.get('game', None)
    
        context = {'event_name': event_name,
                   'game': game,
                   'sorted_team_player_list': request.session.get('sorted_team_player_list', None),
                   'team_name': team,
                   }
    except:
        raise Http404("Event Not Found")
        
    return render(request, 'esports/eventresults.html', context)

def eventInformation(request):
    
    player_name = request.GET.get('player', None)
    game = request.session.get('game', None)
    summary = main.player_search(player_name, game, 5)
    context = { 'summary': summary }
    
    return render(request, 'esports/information.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = form.cleaned_data['name']
            new_comment.email = form.cleaned_data['email']
            new_comment.comment = form.cleaned_data['comment']
            
            new_comment.save()
            form.save_m2m()
            
            messages.success(request, 'Comment Received')
          
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    
    return render(request, 'esports/contact.html', {'form': form})
