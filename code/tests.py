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

if __name__ == '__main__':
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
                  'Hauntzer', 'MikeYeung', 'Bjergsen', 'Zven', 'Mithy',
                  ]
    
    sorted_team_player_list = {'Team Liquid': {'Impact': 'None', 'Xmithie': 'None', 'Pobelter': 'None', 'Doublelift': 'None', 'Olleh': 'None'},
                              'Cloud 9': {'Licorice': 'None', 'Svenskeren': 'None', 'Jensen': 'None', 'Sneaky': 'None', 'Smoothie': 'None'},
                              'Team SoloMid': {'Hauntzer': 'None', 'MikeYeung': 'None', 'Bjergsen': 'None', 'Zven': 'None', 'Mithy': 'None'},
                              }
    
    for team in sorted_team_player_list:
        for player in sorted_team_player_list[team]:
            sorted_team_player_list[team][player] = 'Hi'
            
    print(sorted_team_player_list)
    
    for team in sorted_team_player_list:
        for player in sorted_team_player_list[team]:
            sorted_team_player_list[team][player] = sorted_team_player_list[team][player] + "h"
            
    print(sorted_team_player_list)
    
#    articles_dict = {}
#    pool = Pool(cpu_count() * 2)
#
#    for team in sorted_team_player_list:
#        player_article = {}
#        for player in sorted_team_player_list[team]:
#            player_article[team] = pool.map(event_extractor.get_articles, player_list)
#            articles_dict[team] = player_article
#        
# 
#    print(articles_dict)
#
#    all_summary_dict = {}    
#    for team in articles_dict:
#        player_summary_dict = {}
#        for player in articles_dict[team]:
#            player_summary_dict[player] = article_summarizer.summarize_text(articles_dict[team][player])
#            
#        all_summary_dict[team] = player_summary_dict
#        
#    for team in sorted_team_player_list:
#        for player in sorted_team_player_list[team]:
#            print(player)
#            print(sorted_team_player_list[team][player])
#    os.system('PAUSE')
#def EventExtractorParralleismTest():

def WordProbabilityTest():
    sites = ["https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/"]
    article_extractor = articles.ArticleExtractor('doublelift', 'league of legends', 5)
    #sites = article_extractor.get_websites()
    sources = [article_extractor.parse_websites(site) for site in sites]
    
    article_summarizer = summarization.Summarization(article_extractor.number_of_bullet_points)
    summary = article_summarizer.summarize_text(sources)
    
    for sentence in summary:
        print(u'\u2022 ' + sentence.lstrip("[]1234567890' "))
        