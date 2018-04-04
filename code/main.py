# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:58 2018

@author: brian
"""

import articles
import summarization

from multiprocessing import Pool # Multiprocessing
from multiprocessing import cpu_count

def player_search(query, game, bullets):
    article_extractor = articles.ArticleExtractor(query, game, bullets)
    article_summarizer = summarization.Summarization(article_extractor.number_of_bullet_points)

    sites = article_extractor.get_websites()
    pool = Pool(cpu_count() * 2)
    sources = pool.map(article_extractor.parse_websites, sites)
    pool.close()
    pool.join()  
    
    summary = article_summarizer.summarize_text(sites, sources)
    
    return summary

def event_search(query, game):
    event_extractor = articles.EventSeperator(query, game)
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

    return sorted_team_player_list

def main(search_type, query, game, bullets):
    #if __name__ == '__main__':        
        if search_type == 'player':
            summary = player_search(query, game, bullets)
            
#            print("\n\nSummary:")
#            for sentence in summary:
#                print(u'\u2022 ' + sentence.lstrip("[]1234567890' "))
    
        elif search_type == 'event':
            sorted_team_player_list = event_search(query, game)
            
#            for team in sorted_team_player_list:
#                for player in sorted_team_player_list[team]:
#                    print(player + " Summary:")
#                    for sentence in sorted_team_player_list[team][player]:
#                        print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" "))
#                    print('\n')
        else:
            print("Invalid Parameter")