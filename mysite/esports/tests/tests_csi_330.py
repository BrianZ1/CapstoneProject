# Theses tests are for CSI-330: Software Dev. Methodologies
# We are learning TDD by applying it to a project

# python manage.py test esports.tests.tests_csi_330
# def setUp(self):

from django.test import TestCase, Client
from esports.models import Player, Event

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
    
    def setUp(self):
        self.clent = Client()  
    
#    def test(self):
#        self.fail("Not Implemented")
        
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