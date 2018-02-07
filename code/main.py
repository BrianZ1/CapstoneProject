# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:58 2018

@author: brian
"""

import articles

from multiprocessing import Pool # Multiprocessing
from multiprocessing import cpu_count
from timeit import default_timer as timer # Timer

def get_query():
    #return 'Doublelift'
    return 'IEM Season 11 - Gyeonggi'
    #return '2017 Worlds'

def get_game():
    return 'League of Legends'

def get_number_of_bullet_points():
    return 5

def get_search_type():
    #return 'Player'
    return 'Event'
    
if __name__ == '__main__':
    
    if get_search_type() == 'Player':
        start = timer()
        article_extractor = articles.ArticleExtractor(get_query(), get_game(), get_number_of_bullet_points())
        end = timer()
        print(end - start)
        
#        start = timer()
#        #sites = article_extractor.get_websites()
#        end = timer()
#        print(end - start)
        sites = ['https://lol.gamepedia.com/Doublelift', 'https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/']
        start = timer()
        pool = Pool(cpu_count() * 2)
        sources = pool.map(article_extractor.parse_websites, sites)
        end = timer()
        print(end - start)
        
        start = timer()
        sources = [article_extractor.parse_websites(site) for site in sites]
        end = timer()
        print(end - start)
        #print(sources)
#        start = timer()
#        print(sources)
#        end = timer()
#        print(end - start)
        
    elif get_search_type() == 'Event':
        event_extractor = articles.EventSeperator(get_query(), get_game())
        
        #site = event_extractor.get_website();
        site = 'https://lol.gamepedia.com/IEM_Season_11_-_Gyeonggi'
        team_with_player_names = event_extractor.get_player_names(site)
        
        articles_dict = {}
        pool = Pool(cpu_count())
        
        for team in team_with_player_names:
            player_article = {}
#            for player in team_with_player_names[team]:
#                player_article[player] = event_extractor.get_articles(player)
#            
#            articles_dict[team] = player_article
           
            player_article[team] = pool.map(event_extractor.get_articles, team_with_player_names[team])
            articles_dict[team] = player_article
        print(articles_dict)   