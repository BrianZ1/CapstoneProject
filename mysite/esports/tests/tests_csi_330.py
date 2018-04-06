# Theses tests are for CSI-330: Software Dev. Methodologies
# We are learning TDD by applying it to a project

# cd C:\Users\brian\Desktop\CapstoneProject\mysite
# python manage.py test esports.tests.tests_csi_330

from django.test import TestCase, Client
from esports.models import Player, Event
import esports.views as page
from esports.forms import PlayerSearchForm, EventSearchForm

import sys
sys.path.append(r'..\code')
from main import player_search

# Feature 1
class StoreSearchQueriesTestCase(TestCase):
    
    def setUp(self):
        Player.objects.create(name="test", count=1)
        Event.objects.create(name="test2", count=1)
    
    # Tests for player add
    def test_add_to_player_database(self):
        new_player = Player(name="a", count=1)
        new_player.save()
        
        player_name = Player.objects.get(name="a")
        self.assertTrue(player_name)
        
        self.assertEqual(player_name.name, "a")
    
    def test_increase_count_for_player_database(self):
        player = Player.objects.get(name="test")
        player.increment_count()
        self.assertEqual(player.count, 2)
    
    # Tests for event add
    def test_add_to_event_database(self):
        new_event = Event(name="a", count=1)
        new_event.save()
        
        event_name = Event.objects.get(name="a")
        self.assertTrue(event_name)
        
        self.assertEqual(event_name.name, "a")
    
    def test_increase_count_for_event_database(self):
        event = Event.objects.get(name="test2")
        event.increment_count()
        self.assertEqual(event.count, 2)
        
# Feature 2
class DisplayTopSearchQueriesTestCase(TestCase):
    
    def populate_database(self, database_object):
        database_object.objects.create(name="test", count=1)
        database_object.objects.create(name="test2", count=2)
        database_object.objects.create(name="test3", count=7)
        database_object.objects.create(name="test4", count=4)
        database_object.objects.create(name="test5", count=5)
        
        return database_object
        
    def setUp(self):
        self.clent = Client()
    
    # Test for home page
    def test_home_view(self):
        response = self.client.get('//')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/home.html')
    
    # Tests for player display
    def test_get_top_5_players(self):
        players = self.populate_database(Player)
        
        player_list = page.get_top_5_item_searches(players)
        self.assertEqual(len(player_list), 5)
        self.assertEqual([player.count for player in player_list], [7,5,4,2,1])
        
    def test_players_display(self):
        players = self.populate_database(Player)
        player_list = page.get_top_5_item_searches(players)
        
        response = self.client.get('//')

        self.assertEqual(len(response.context['player_list']), 5)
        self.assertQuerysetEqual(response.context['player_list'], player_list, transform=lambda x: x)
        
    def test_players_html(self):
        response = self.client.get('//')               
        self.assertContains(response, "<h2>Top 5 Searched Players</h2>", html=True)
        
    def test_0_players_in_database(self):
        response = self.clent.get('//')
        self.assertFalse(page.get_top_5_item_searches(Player))
        self.assertContains(response, "<p>No Players Found</p>", html=True)
        
    # Tests for events display
    def test_get_top_5_events(self):
        events = self.populate_database(Event)
        
        event_list = page.get_top_5_item_searches(events)
        self.assertEqual(len(page.get_top_5_item_searches(events)), 5)
        self.assertEqual([event.count for event in event_list], [7,5,4,2,1])
        
    def test_event_display(self):
        events = self.populate_database(Event)
        event_list = page.get_top_5_item_searches(events)
        
        response = self.client.get('//')
                
        self.assertEqual(len(response.context['event_list']), 5)
        self.assertQuerysetEqual(response.context['event_list'], event_list, transform=lambda x: x)
        
    def test_event_html(self):
        response = self.client.get('//')
        self.assertContains(response, "<h2>Top 5 Searched Events</h2>", html=True)
        
    def test_0_events_in_database(self):
        response = self.client.get('//')
        self.assertFalse(page.get_top_5_item_searches(Event))
        self.assertContains(response, "No Events Found", html=True)
        
# Feature 3
class MoreOptionsInFormsTestCase(TestCase):
    
    def setUp(self):
        self.client = Client() 
        self.player_response = self.client.get('/playersearch/')
        self.event_response = self.client.get('/eventsearch/')
        
    def test_display_league_option(self):
        self.assertContains(self.player_response,
                            '<option value="league of legends">Leauge of Legends</option>',
                            html=True)   
        self.assertContains(self.event_response,
                            '<option value="league of legends">Leauge of Legends</option>',
                            html=True)   
       
    def test_display_csgo_option(self):
        self.assertContains(self.player_response,
                            '<option value="counter-strike: global offensive">Counter-Strike: Global Offensive</option>',
                            html=True)   
        
        self.assertContains(self.event_response,
                            '<option value="counter-strike: global offensive">Counter-Strike: Global Offensive</option>',
                            html=True)  
        
    def test_display_Dota2_option(self):
        self.assertContains(self.player_response,
                            '<option value="dota 2">Dota 2</option>',
                            html=True)   
        
        self.assertContains(self.event_response,
                            '<option value="dota 2">Dota 2</option>',
                            html=True) 
        
    def test_display_Overwatch_option(self):
        self.assertContains(self.player_response,
                            '<option value="overwatch">Overwatch</option>',
                            html=True)   
        
        self.assertContains(self.event_response,
                            '<option value="overwatch">Overwatch</option>',
                            html=True) 

    def test_display_Heroes_option(self):
        self.assertContains(self.player_response,
                            '<option value="heroes of the storm">Heroes of the Storm</option>',
                            html=True)   
        
        self.assertContains(self.event_response,
                            '<option value="heroes of the storm">Heroes of the Storm</option>',
                            html=True) 
        
    def test_save_game_type_option_player(self):
        form = PlayerSearchForm({
                'player_name' : 'test', 
                'game' : 'counter-strike: global offensive',
                'num_articles': 5,
                })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['game'], 'counter-strike: global offensive')
    
    def test_save_game_type_option_event(self):
        form = EventSearchForm({
                'event_name' : 'test', 
                'game' : 'counter-strike: global offensive',
                'num_articles': 5,
                })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['game'], 'counter-strike: global offensive')
        
# Feature 4
class AddExtraSentenceToSummaryTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()    
    
    def test_initial_summary(self):
        articles = player_search('doublelift', 'league of legends', 2)
        
        self.assertEquals(len(articles), 2)
        
        short_article = page.get_summary_of_length(articles, 5)
        for article in short_article:
            self.assertEquals(len(short_article[article]), 5)
         
    def test_extra_summary_button_functionality(self):
        test_summary = {'test': ['1', '2', '3', '4', '5', '6', '7', '8']}
        
        session = self.client.session
        
        page.increment_sentence_length(session, 7)
        short_test_summary = page.get_summary_of_length(test_summary, session["summary_length"] )
        for article in short_test_summary:
            self.assertEquals(len(short_test_summary[article]), 8)
        
    def test_no_more_summary(self):
        test_summary = {'test': ['1', '2', '3', '4', '5']}
        
        short_test_summary = page.get_summary_of_length(test_summary, 7)
        for article in short_test_summary:
            self.assertEquals(len(short_test_summary[article]), 5)
        
    def test_not_enough_summary(self):
        test_summary = {'test': ['1', '2', '3', '4']}
        
        short_test_summary = page.get_summary_of_length(test_summary, 5)
        for article in short_test_summary:
            self.assertLessEqual(len(short_test_summary[article]), 5)
            self.assertListEqual(short_test_summary[article], ['Not Enough Information from Site'])