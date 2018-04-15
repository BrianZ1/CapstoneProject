# Unit tests

# cd C:\Users\brian\Desktop\CapstoneProject\mysite
# python manage.py test esports.tests.code_tests

from django.test import TestCase, Client

import esports.code.articles
import esports.code.naive_bayes_classifier
import esports.code.nltk_opperations
import esports.code.summarization

# Create your tests here.

class ArticlesTestCase(TestCase):
    
    def setUp(self):
        pass
    
    def test(self):
        pass
    
class NaiveBayesClassifierTestCase(TestCase):
    
    def test(self):
        pass
    
class NLTKTestCase(TestCase):
    
    def test(self):
        pass
    
class SummarizationTestCase(TestCase):
    
    def test(self):
        pass   
    
class ContactFormTestCase(TestCase):
    
    def test(self):
        pass
    