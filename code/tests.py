# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:37:04 2018

@author: brian
"""
import articles
import summarization
from multiprocessing import Pool # Multiprocessing
from multiprocessing import cpu_count
import os
from timeit import default_timer as timer # Timer
import main
'''
        start = timer()
        end = timer()
        print(end - start)
'''
from naive_bayes_classifier import NaiveBayesClassifier

if __name__ == '__main__':
    summary = main.player_search('doublelift', 'league of legends', 5)

    for sentence in summary:
        print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" ")) 
    print('\n')

def NBCTest():        
    nbc = NaiveBayesClassifier()
    
    sites = ["https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/"]
    article_extractor = articles.ArticleExtractor('doublelift', 'league of legends', 5)
    #sites = article_extractor.get_websites()
    article = [article_extractor.parse_websites(site) for site in sites]
    
    string_text = list_to_string(article)
    string_text = string_text.replace("', '", ' ')
    string_text = string_text.replace('", "', ' ')
    
    summary = nbc.get_summary(string_text, 5)
    
    print("Summary:")
    for sentence in summary:
        print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" ")) 

def EventExtractorParralleismTest():
    event_extractor = articles.EventSeperator('IEM Season 11 - Gyeonggi', 'league of legends')
    article_summarizer = summarization.Summarization(5)

    #site = event_extractor.get_website();
    #site = 'https://lol.gamepedia.com/IEM_Season_11_-_Gyeonggi'
    #sorted_team_player_list, player_list = event_extractor.get_player_team_names(site)
    
#    sorted_team_player_list = {'Team Liquid': ['Impact', 'Xmithie', 'Pobelter', 'Doublelift', 'Olleh'],
#                              'Cloud 9': ['Licorice', 'Svenskeren', 'Jensen', 'Sneaky', 'Smoothie'],
#                              'Team SoloMid': ['Hauntzer', 'MikeYeung', 'Bjergsen', 'Zven', 'Mithy'],
#                             }
    
    player_list = ['Impact', 'Xmithie', 'Pobelter', 'Doublelift', 'Olleh',
                  'Licorice', 'Svenskeren', 'Jensen', 'Sneaky', 'Smoothie',
                  'Hauntzer', 'MikeYeung', 'Bjergsen', 'Zven', 'Mithy'
                  ]
    
    sorted_team_player_list = {'Team Liquid': {'Impact': 'None', 'Xmithie': 'None', 'Pobelter': 'None', 'Doublelift': 'None', 'Olleh': 'None'},
                              'Cloud 9': {'Licorice': 'None', 'Svenskeren': 'None', 'Jensen': 'None', 'Sneaky': 'None', 'Smoothie': 'None'},
                              'Team SoloMid': {'Hauntzer': 'None', 'MikeYeung': 'None', 'Bjergsen': 'None', 'Zven': 'None', 'Mithy': 'None'},
                              }
    
    pool = Pool(cpu_count() * 2)
    player_articles = pool.map(event_extractor.get_articles, player_list)
    pool.close()
    pool.join()

    index = 0
    for team in sorted_team_player_list:
        for player in sorted_team_player_list[team]:
            sorted_team_player_list[team][player] = player_articles[index]
            index += 1
 
    for team in sorted_team_player_list:
        for player in sorted_team_player_list[team]:
            sorted_team_player_list[team][player] = article_summarizer.summarize_text(sorted_team_player_list[team][player])
        
    for team in sorted_team_player_list:
        for player in sorted_team_player_list[team]:
            print(player + " Summary:")
            for sentence in sorted_team_player_list[team][player]:
                print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" "))
                print('\n')
                
def WordProbabilityParrallelismTest():
    article_extractor = articles.ArticleExtractor('doublelift', 'league of legends', 8)

    sites = article_extractor.get_websites()
    pool = Pool(cpu_count() * 2)
    sources = pool.map(article_extractor.parse_websites, sites)
    pool.close()
    pool.join()
    
    article_summarizer = summarization.Summarization(article_extractor.number_of_bullet_points)
    
    summary = article_summarizer.summarize_text(sources)
    
    for sentence in summary:
        print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" "))
                
def WordProbabilityTest():
    sites = ["https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/"]
    article_extractor = articles.ArticleExtractor('doublelift', 'league of legends', 5)
    #sites = article_extractor.get_websites()
    sources = [article_extractor.parse_websites(site) for site in sites]
    
    article_summarizer = summarization.Summarization(article_extractor.number_of_bullet_points)
    summary = article_summarizer.summarize_text(sources)
    
    for sentence in summary:
        print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" "))
        
        
def list_to_string(article):
    return ''.join(str(text) for text in article)