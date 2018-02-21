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
        sorted_team_player_list, player_list = event_extractor.get_player_team_names(site)
        
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
    
    else:
        print("Invalid Parameter")