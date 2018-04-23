# Unit tests

# cd C:\Users\brian\Desktop\CapstoneProject\mysite
# python manage.py test esports.tests.code_tests

from django.test import TestCase, Client

import esports.code.articles as articles
import esports.code.naive_bayes_classifier as nbc
import esports.code.nltk_opperations as nltk
import esports.code.summarization as summarization

# Create your tests here.

class ArticlesTestCase(TestCase):
    
    def setUp(self):
        self.articles = articles.ArticleExtractor('doublelift', 'league of legends', 1 , None, None)
        self.events = articles.EventSeperator('2017 worlds', 'league of legends', 1)
    
    def test_article_init(self):
        self.assertEqual(self.articles.player_name, 'doublelift')
        self.assertEqual(self.articles.game_name, 'league of legends')
        self.assertEqual(self.articles.num_articles, 1)
        self.assertEqual(self.articles.start_date, None)
        self.assertEqual(self.articles.end_date, None)
        
    def test_get_one_website(self):
        self.assertEqual(len(self.articles.get_websites()), 1)
    
    def test_parse_website(self):
        url = 'https://www.invenglobal.com/articles/4820/league-of-legends-esports-captain-america-doublelift-will-na-leave-their-mark-at-msi'
        self.assertTrue(self.articles.parse_websites(url))
    
    def test_event_init(self):
        self.assertEqual(self.events.event_name, '2017 worlds')
        self.assertEqual(self.events.event_game, 'league of legends')
        self.assertEqual(self.events.number_articles, 1)
        
    def test_get_event_website(self):
        self.assertTrue(self.events.get_website())
    
    def test_get_player_team_name(self):
        url = 'http://liquipedia.net/leagueoflegends/World_Championship/2017'
        temp = self.events.get_player_team_names(url)
        self.assertTrue(temp)
        self.assertEquals(type(temp), dict)
        
    def test_get_event_name(self):
        self.assertEquals(self.events.get_event_name(), '2017 World Championship')
    
    def test_get_event_time(self):
        url = 'http://liquipedia.net/leagueoflegends/World_Championship/2017'
        self.assertEquals(self.events.get_event_time_period(url), ('2017-09-23', '2017-11-04') )
    
class NaiveBayesClassifierTestCase(TestCase):
    
    def setUp(self):
        self.classifier = nbc.NaiveBayesClassifier()
        self.list_text = ['This', 'is', '1', 'Big', 'test']
        self.text = 'This is 1 Big test'
    
    def test_load_classifier(self):
        self.assertTrue(nbc.load_classifier())
        
    def test_list_to_string(self):
        self.assertEqual(nbc.list_to_string(self.list_text), self.text)
    
    def test_clean_article(self):
        self.assertEqual(nbc.clean_article_sites(self.text), ['this', '1', 'big', 'test'])
        
    def test_get_features(self):
        features = nbc.get_features(self.text, self.text)
        
        self.assertEqual(len(features), 6)
        
        self.assertTrue(features['sentence_length'])
        self.assertEqual(features['sentence_length'], 18)
        
        self.assertTrue(features['num_words'])
        self.assertEqual(features['num_words'], 4)
        
        self.assertTrue(features['capital_words'])
        self.assertEqual(features['capital_words'], 2)
        
        self.assertTrue(features['numbers'])
        self.assertEqual(features['numbers'], 1)
        
        self.assertTrue(features['adjective_count'])
        self.assertEqual(features['adjective_count'], 1)
        
        self.assertTrue(features['word_freq'])
        self.assertAlmostEqual(features['word_freq'], .25)
        
    def test_calculate_sentence_score(self):
        test_dict = self.classifier.calculate_sentence_score(['test', 'test2'], [self.list_text, self.list_text])
        self.assertTrue(test_dict)
        self.assertEqual(len(test_dict), 2)
    
class SummarizationTestCase(TestCase):
    
    def setUp(self):
        self.summarize = summarization.Summarization()
    
    def test_init(self):
        self.assertEqual(self.summarize.summary_length, 5)
    
    def test_summary_no_article(self):
        self.assertEqual(self.summarize.summarize_text(['test'], []), ["Not enought information about player"])
    