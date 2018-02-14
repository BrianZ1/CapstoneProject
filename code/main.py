# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:58 2018

@author: brian
"""

import articles

from multiprocessing import Pool # Multiprocessing
from multiprocessing import cpu_count

from timeit import default_timer as timer # Timer
#        start = timer()
#        end = timer()
#        print(end - start)
import sys

def get_query():
#    return input("Enter Search Item: ")
    
    return 'Doublelift'
    #return 'IEM Season 11 - Gyeonggi'
    #return '2017 Worlds'

def get_game():
#    return input("Enter Game: ").lower()
    
    return 'league of legends'

def get_number_of_bullet_points():
#    return input("Number of Bullet Points: ")
    
    return 5

def get_search_type(args):
#    if(len(args) == 2):
#        if(args[1].lower() == 'player' or args[1].lower() == 'event'):
#            return args[1].lower()
#        else:
#            return None
    
    return 'player'
    #return 'event'
    
if __name__ == '__main__':
        
    if get_search_type(sys.argv) == 'player':
        article_extractor = articles.ArticleExtractor(get_query(), get_game(), get_number_of_bullet_points())
    
        sites = article_extractor.get_websites()
        #sites = ['https://lol.gamepedia.com/Doublelift', 'https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/']
        pool = Pool(cpu_count() * 2)
        sources = pool.map(article_extractor.parse_websites, sites)
    
        #sources = [article_extractor.parse_websites(site) for site in sites]
        
        print(sources)

    elif get_search_type(sys.argv) == 'event':
        event_extractor = articles.EventSeperator(get_query(), get_game())
        
        site = event_extractor.get_website();
        #site = 'https://lol.gamepedia.com/IEM_Season_11_-_Gyeonggi'
        team_with_player_names = event_extractor.get_player_names(site)
        
        articles_dict = {}
        pool = Pool(cpu_count() * 2)
        
        for team in team_with_player_names:
            player_article = {}
#            for player in team_with_player_names[team]:
#                player_article[player] = event_extractor.get_articles(player)
#            
#            articles_dict[team] = player_article
           
            player_article[team] = pool.map(event_extractor.get_articles, team_with_player_names[team])
            articles_dict[team] = player_article
 
    else:
        print("Invalid Parameter")