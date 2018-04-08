from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('playersearch/', views.playerSearch, name='playersearch'),
    path('playersearch/<str:game>/<str:player_name>', views.playerResults, name='playerresults'),
    path('eventsearch/', views.eventSearch, name='eventsearch'),
    path('eventsearch/<str:game>/<str:event_name>/', views.eventResults, name='eventresults'),
    path('eventsearch/<str:game>/<str:event_name>/<str:team>', views.eventResultsTeam, name='eventresultsteam'),
    url(r'^ajax/eventinformation/$', views.eventInformation, name='eventinformation'),
    path('summarylength/', views.increment_summary_length, name='summarylength'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),      
    
]
