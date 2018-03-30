# Theses tests are for CSI-330: Software Dev. Methodologies
# We are learning TDD by applying it to a project

# python manage.py test esports.tests.tests_csi_330
# def setUp(self):

from django.test import TestCase, Client
from esports.models import Player, Event
import esports.views as page

# Feature 1
class StoreSearchQueriesTestCase(TestCase):
    
    def setUp(self):
        Player.objects.create(name="test", count=1)
        Event.objects.create(name="test2", count=1)
    
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
        
    def test_home_view(self):
        response = self.client.get('//')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/home.html')
    
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
        
## Feature 3
#class Feature3TestCase(TestCase):
#    
#    def setUp(self):
#        pass    
#    
#    def test(self):
#        self.fail("Not Implemented")          
#        
## Feature 4
#class Feature4TestCase(TestCase):
#    
#    def setUp(self):
#        pass    
#    
#    def test(self):
#        self.fail("Not Implemented")