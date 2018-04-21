# Website tests

# cd C:\Users\brian\Desktop\CapstoneProject\mysite
# python manage.py test esports.tests.web_tests

from django.test import TestCase, Client
from esports.forms import ContactForm

from esports.code.main import player_search
from esports.views import get_summary_of_length

class WebPageTestCase(TestCase):
    
    def setUp(self):
        self.clent = Client()
    
    def test_home_view(self):
        response = self.client.get('/esports/')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/home.html')
    
    def test_player_view(self):
        response = self.client.get('/playersearch/')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/playersearch.html')
        
    def test_event_view(self):
        response = self.client.get('/eventsearch/')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/eventsearch.html')    
   
    def test_about_view(self):
        response = self.client.get('/about/')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/about.html')   
        
    def test_contact_view(self):
        response = self.client.get('/contact/')
                
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esports/contact.html')
    
class ContactFormTestCase(TestCase):
    
    def test_contact_from(self):
        form = ContactForm({
                'name' : 'test_name', 
                'email' : 'test_email@testsite.com',
                'comment': 'test_comment',
                })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['name'], 'test_name')
        self.assertEqual(form.cleaned_data['email'], 'test_email@testsite.com')
        self.assertEqual(form.cleaned_data['comment'], 'test_comment')
        
class PlayerSearchTestCase(TestCase):
    
    def test_player_search(self):
        summary = player_search('doublelife', 'league of legends', 1, None, None)
        shortened_summary = get_summary_of_length(summary, 5)

        self.assertEqual(len(shortened_summary), 1)
