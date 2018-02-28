from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('playersearch/', views.playerSearch, name='playersearch'),
    path('playersearch/<str:name>/', views.playerResults, name='playerresults'),
    path('eventsearch/', views.eventSearch, name='eventsearch'),
    path('eventsearch/<str:name>/', views.eventResults, name='eventresults'),
    path('contact/', views.contact, name='contact'),      
    
]
