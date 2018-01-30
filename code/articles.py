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
    
        for site in googlesearch.search(self.player_name, tld="com", num=1, start=0, stop=2, pause=2):
            
            if '#' in site or 'youtube' in site or 'twitter' \
                in site or 'facebook' in site or 'urbandictionary' in site:
                continue
            
            if "com" in site:
                sites.append(site)

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
        site = self.get_website();
        team_names = self.get_teams(site);
        team_with_player_names = self.get_player_names(site, team_names)
        
        for team in team_with_player_names:
            print(team)
            for player in team_with_player_names[team]:
                print(player)
                
        return None
    
    '''
    Uses gamepedia for event information
    Returns main webpage for event
    '''
    def get_website(self):
        for site in googlesearch.search((self.event_name + 'gamepedia'), tld="com", num=1, start=0, stop=1, pause=2):
            return site
        
    '''
    Returns the teams attending / attended an event
    '''
    def get_teams(self, site):
        html = request.urlopen(site).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
        
        teams_table = soup.find("table", {"class":"prettytable"})
        found_teams = teams_table.find_all("span", {"class":"teamLongTitle"})
                
        teams = [team.text for team in found_teams]
        return sorted(teams, key=str.lower)
        
    '''
    Returns individual players seperated by team
    '''
    def get_player_names(self, site, team_names):        
        html = request.urlopen(site + "/Team_Rosters").read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
  
        team_with_player_name = {}
    
        all_team_table = soup.find_all("table", {"class":"prettytable"})
        
        # Check for number of teams matches number of table
        if len(team_names) != len(all_team_table):
            print("Number of teams do not match number of tables.")
            return None
        
        # Go through each table
        for team_table, team_names in zip(all_team_table, team_names):            
            data = []

            # Seperate by row / column for player name
            rows = team_table.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
            
            # New table of just player names
            player_names = [player[0] for player in data if len(player) == 2]
            
            team_with_player_name[team_names] = player_names
        
        return team_with_player_name
    
    '''
    Get articles for player
    '''
    def get_articles(self, name):
        return None
        