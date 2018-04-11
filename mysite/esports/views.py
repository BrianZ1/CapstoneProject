from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from .forms import PlayerSearchForm, EventSearchForm, ContactForm
from .models import Player, Event

from random import randint
from time import sleep

from .code.main import player_search
from .code.articles import EventSeperator

def home(request):
    request.session.flush()
    
    context = {
            'player_list': get_top_5_item_searches(Player),
            'event_list': get_top_5_item_searches(Event),
            }
    
    return render(request, 'esports/home.html', context)

def playerSearch(request):    
    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        
        if form.is_valid():
            request.session['player_name'] = form.cleaned_data['player_name']
            request.session['game'] = form.cleaned_data['game']
            request.session['num_articles'] = form.cleaned_data['num_articles']
            request.session['summary_length'] = 5
            
            if 'summary' in request.session:
                del request.session['summary']
  
            check_player = Player.objects.filter(name=form.cleaned_data['player_name'].lower(), game=form.cleaned_data['game'].lower())
            
            if len(check_player) == 0:
                new_player = Player(name=form.cleaned_data['player_name'].lower(), game=form.cleaned_data['game'].lower(), count = 1)
                new_player.save()
            else:
                player = Player.objects.get(name=form.cleaned_data['player_name'].lower(), game=form.cleaned_data['game'].lower())
                player.increment_count()
                player.save()
                          
            return HttpResponseRedirect('/esports/playersearch/' + request.session.get('game', None) + '/' + request.session.get('player_name', None))
    else:
        form = PlayerSearchForm()

    return render(request, 'esports/playersearch.html', {'form': form})

def playerResults(request, game, player_name):
    try:
        num_articles = request.session.get('num_articles', 5)
        summary_length = request.session.get('summary_length', 5)
        request.session['summary_length'] = summary_length
       
        if 'summary' in request.session:
            summary = request.session["summary"]
        else:
            summary = player_search(player_name, game, num_articles, None, None)
            request.session["summary"] = summary
            
        shortened_summary = get_summary_of_length(summary, summary_length)
        
        context = {'player_name': player_name, 'summary': shortened_summary}
    except:
        raise Http404("Player Not Found")
  
    return render(request, 'esports/playerresults.html', context)

def eventSearch(request):
    if request.method == 'POST':
        form = EventSearchForm(request.POST)
        
        if form.is_valid():
            request.session['game'] = form.cleaned_data['game']
            request.session['num_articles'] = form.cleaned_data['num_articles']
            request.session['summary_length'] = 5
            
            event_extractor = EventSeperator(form.cleaned_data['event_name'], request.session['game'])
            event_name = event_extractor.get_event_name()
            request.session['event_name'] = event_name
            
            check_event = Event.objects.filter(name=event_name.lower(), game=form.cleaned_data['game'].lower())
            
            if len(check_event) == 0:
                new_event = Event(name=event_name.lower(), game=form.cleaned_data['game'].lower(), count = 1)
                new_event.save()
            else:
                event = Event.objects.get(name=event_name.lower(), game=form.cleaned_data['game'].lower())
                event.increment_count()
                event.save()
                
            return HttpResponseRedirect('/esports/eventsearch/' + request.session.get('game', None) + '/' + event_name)
    else:
        form = EventSearchForm()
        
    return render(request, 'esports/eventsearch.html', {'form': form})

def eventResults(request, game, event_name):
    try:
        num_articles = request.session.get('num_articles', 5)
        
        event_extractor = EventSeperator(event_name, game, num_articles)

        site, date = event_extractor.get_website();
        sorted_team_player_list = event_extractor.get_player_team_names(site)
              
        request.session['sorted_team_player_list'] = sorted_team_player_list
        team = next(iter(sorted_team_player_list))
        request.session['team'] = team
        request.session['start_date'] = date[0]
        request.session['end_date'] = date[1]
    
        context = {'event_name': event_name,
                   'game': game,
                   'sorted_team_player_list': sorted_team_player_list,
                   'team_name': team,
                   }
    except:
        raise Http404("Event Not Found")
        
    return render(request, 'esports/eventresults.html', context)

def eventResultsTeam(request, game, event_name, team):
    try:    
        context = {'event_name': event_name,
                   'game': game,
                   'sorted_team_player_list': request.session.get('sorted_team_player_list', None),
                   'team_name': team,
                   }
    except:
        raise Http404("Event Not Found")
        
    return render(request, 'esports/eventresults.html', context)

def eventInformation(request):
    
    sleep(randint(0,10))
    
    player_name = request.GET.get('player', None)
    game = request.GET.get('game', None)
    num_articles = request.session.get('num_articles', 5)
    summary_length = request.session.get('summary_length', 5)
    start_date = request.session.get('start_date', None)
    end_date = request.session.get('end_date', None)

    summary = player_search(player_name, game, num_articles, start_date, end_date)
    shortened_summary = get_summary_of_length(summary, summary_length)   
    context = { 'summary': shortened_summary }
    
    return render(request, 'esports/information.html', context)

def increment_summary_length(request):
    increment_sentence_length(request.session, request.session["summary_length"])    
    return HttpResponse(status=201)

def about(request):    
    return render(request, 'esports/about.html')

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

def get_top_5_item_searches(database):
    return database.objects.order_by('-count')[:5]

def get_summary_of_length(articles_dict_old, length):
        articles_dict = articles_dict_old.copy()
    
        for sentence_dict in articles_dict:
            if(len(articles_dict[sentence_dict]) < 5):
                articles_dict[sentence_dict] = ["Not Enough Information from Site"]
            else:
                articles_dict[sentence_dict] = articles_dict[sentence_dict][:length]
        
        return articles_dict
    
def increment_sentence_length(session, length):
    session["summary_length"] = length + 1
    
