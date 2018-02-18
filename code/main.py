# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:58 2018

@author: brian
"""

import articles
import summarization

from multiprocessing import Pool # Multiprocessing
from multiprocessing import cpu_count

from timeit import default_timer as timer # Timer
#        start = timer()
#        end = timer()
#        print(end - start)
import sys

def get_query():
   return input("Enter Search Item: ")

def get_game():
    return input("Enter Game: ").lower()

def get_number_of_bullet_points():
    return input("Number of Bullet Points: ")

def get_search_type(args):
    if(len(args) == 2):
        if(args[1].lower() == 'player' or args[1].lower() == 'event'):
            return args[1].lower()
        else:
            return None
    
if __name__ == '__main__':
        
    if get_search_type(sys.argv) == 'player':
        article_extractor = articles.ArticleExtractor(get_query(), get_game(), get_number_of_bullet_points())
    
        sites = article_extractor.get_websites()
        pool = Pool(cpu_count() * 2)
        sources = pool.map(article_extractor.parse_websites, sites)
        
        article_summarizer = summarization.Summarization(article_extractor.number_of_bullet_points)
        
        summary = article_summarizer.summarize_text(sources)
        
        print("\n\nSummary:")
        for sentence in summary:
            print(u'\u2022 ' + sentence.lstrip("[]1234567890' "))

    elif get_search_type(sys.argv) == 'event':
        event_extractor = articles.EventSeperator(get_query(), get_game())
        article_summarizer = summarization.Summarization(5)

        site = event_extractor.get_website();
        team_with_player_names = event_extractor.get_player_team_names(site)
        
        articles_dict = {}
        pool = Pool(cpu_count() * 2)
        
        for team in team_with_player_names:
            player_article = {}
            for player in team_with_player_names[team]:
                player_article[player] = event_extractor.get_articles(player)
            
            articles_dict[team] = player_article
           
#            player_article[team] = pool.map(event_extractor.get_articles, team_with_player_names[team])
#            articles_dict[team] = player_article
            
        all_summary_dict = {}    
        for team in articles_dict:
            player_summary_dict = {}
            for player in articles_dict[team]:
                player_summary_dict[player] = article_summarizer.summarize_text(articles_dict[team][player])
                
            all_summary_dict[team] = player_summary_dict
    
    else:
        print("Invalid Parameter")