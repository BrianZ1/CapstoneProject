from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('playersearch/', views.playerSearch, name='playersearch'),
    path('playerresults/', views.playerResults, name='playerresults'),
    path('eventsearch/', views.eventSearch, name='eventsearch'),
    path('eventresults/', views.eventResults, name='eventresults'),
    path('contact/', views.contact, name='contact'),      
]
