# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:00:45 2018

@author: brian

"""

# Parser
from bs4 import BeautifulSoup
from urllib import request

# Google Search
import googlesearch

class ArticleExtractor:

    '''
    Init class with player name to search
    '''
    def __init__(self, name):
        self.player_name = name
        print(name)
        
    '''
    Main function, returns x articles
    '''
    def get_articles(self):
        sites = self.get_websites()
    
        sources = []
        for site in sites:
            sources.append(self.parse_websites(site))
            
        return sources
    
    '''
    Uses google api to get a list of sites
    '''    
    def get_websites(self):
        sites = []
    
        for j in googlesearch.search(self.player_name, tld="com", num=1, start=0, stop=2, pause=2):
            
            if '#' in j or 'youtube' in j or 'twitter' \
                in j or 'facebook' in j or 'urbandictionary' in j:
                continue
            
            if "com" in j:
                sites.append(j)

        return sites

    '''
    Uses beautiful soup to parse given url. 
    '''
    def parse_websites(self, url):
        paragraph = []
        
        html = request.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
        
        for p in soup.find_all('p'):
            paragraph.append(p.text)
            
        return paragraph
    

class EventSeperator:
    '''
    Init class with event name and game to search
    '''
    def __init__(self, name, game):
        self.event_name = name
        self.event_game = game
        print(name)
        
    '''
    Creates article extractor for each player and returns articles
    '''
    def get_players(self):

        return self.get_teams()
        
    '''
    Returns the teams attending / attended an event
    https://lol.gamepedia.com/2017_Season_World_Championship
    '''
    def get_teams(self):
        for j in googlesearch.search((self.event_name + 'gamepedia'), tld="com", num=1, start=0, stop=1, pause=2):
            site = j
        
        html = request.urlopen(site).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
        
        teams_table = soup.find("table", {"class":"prettytable"})
        found_teams = teams_table.find_all("span", {"class":"teamLongTitle"})
                
        return [t.text for t in found_teams]
        
    '''
    Returns individual players from team
    https://lol.gamepedia.com/2016_Season_World_Championship/Team_Rosters
    '''
    def get_players_info(self, team_name):
        return None
        

        
        
        