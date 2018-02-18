# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:53:47 2018

@author: brian
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:58 2018

@author: brian
"""

import articles
import summarization

from multiprocessing import Pool # Multiprocessing
from multiprocessing import cpu_count

import sys
import os 

def get_query():
    #return 'IEM Season 11 - Gyeonggi'
    #return 'Doublelift'
    return input("Enter Search Item: ")

def get_game():
    #return 'league of legends'
    return input("Enter Game: ").lower()

def get_number_of_bullet_points():
    #return 5
    return input("Number of Bullet Points: ")

def get_search_type(args):
    return 'player'
    if(len(args) == 2):
        if(args[1].lower() == 'player' or args[1].lower() == 'event'):
            return args[1].lower()
        else:
            return None
    
if __name__ == '__main__':
        
    if get_search_type(sys.argv) == 'player':
        # Article Extractor Stuff
        article_extractor = articles.ArticleExtractor(get_query(),
                                                      get_game(),
                                                      get_number_of_bullet_points())

        sites = article_extractor.get_websites()

        pool = Pool(cpu_count() * 2)
        sources = pool.map(article_extractor.parse_websites, sites)
        
        # Text Summarization Stuff
        article_summarizer = summarization.Summarization(article_extractor.number_of_bullet_points)
        
        summary = article_summarizer.summarize_text(sources)
        
        # Display Stuff
        print("\n\nSummary:")
        for sentence in summary:
            print(u'\u2022 ' + sentence.lstrip("[]1234567890' "))

    elif get_search_type(sys.argv) == 'event':
        event_extractor = articles.EventSeperator(get_query(), get_game())
        
        site = event_extractor.get_website();
        
        team_with_player_names = event_extractor.get_player_team_names(site)

        articles_dict = {}
        pool = Pool(cpu_count() * 2)
        
        for team in team_with_player_names:
            player_article = {}
           
            player_article[team] = pool.map(event_extractor.get_articles,
                          team_with_player_names[team])
            articles_dict[team] = player_article
              
    else:
        print("Invalid Parameter")