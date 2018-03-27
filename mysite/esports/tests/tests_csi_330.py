# Theses tests are for CSI-330: Software Dev. Methodologies
# We are learning TDD by applying it to a project

# python manage.py test esports.tests.tests_csi_330
# def setUp(self):

from django.test import TestCase, Client
from esports.models import Player, Event

# Feature 1
class StoreSearchQueriesTestCase(TestCase):
    
    def setUp(self):
        Player.objects.create(name="test", count=0)
    
    def test_add_to_player_database(self):
        new_player = Player(name="a", count=0)
        new_player.save()
        
        player_name = Player.objects.get(name="a")
        self.assertTrue(player_name)
        
        self.assertEqual(player_name.name, "a")
    
    def test_increase_count_for_player_database(self):
        self.fail("Not Implemented")
    
    def test_add_to_event_database(self):
        self.fail("Not Implemented")
    
    def test_increase_count_for_event_database(self):
        self.fail("Not Implemented")
    
        
# Feature 2
class DisplayTopSearchQueriesTestCase(TestCase):
    
    def setUp(self):
        self.clent = Client()  
    
    def test(self):
        self.fail("Not Implemented")
        
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