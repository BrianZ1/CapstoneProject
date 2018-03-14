from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('playersearch/', views.playerSearch, name='playersearch'),
    path('playersearch/<str:name>/', views.playerResults, name='playerresults'),
    path('eventsearch/', views.eventSearch, name='eventsearch'),
    path('eventsearch/<str:name>/', views.eventResults, name='eventresults'),
    path('eventsearch/<str:name>/<str:team>', views.eventResultsTeam, name='eventresultsteam'),
    url(r'^ajax/eventinformation/$', views.eventInformation, name='eventinformation'),
    path('contact/', views.contact, name='contact'),      
    
]
