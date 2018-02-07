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
    def __init__(self, name, game, bullet_points = 5):
        self.player_name = name
        self.game_name = game
        self.number_of_bullet_points = 5
        print(name)
    
    '''
    Uses google api to get a list of sites
    '''    
    def get_websites(self):
        sites = []
        for site in googlesearch.search(self.player_name + self.game_name, tld="com", lang='en', num=1, start=0, stop=1, pause=2):
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

        try:
            html = request.urlopen(url).read().decode('utf8')
            soup = BeautifulSoup(html, "lxml")
        
            for p in soup.find_all('p'):
                paragraph.append(p.text)
        except:
            paragraph.append("")
               
        return paragraph
    

class EventSeperator:
    '''
    Init class with event name and game to search
    '''
    def __init__(self, name, game):
        self.event_name = name
        self.event_game = game
        self.number_of_bullet_points = 5
        print(name)
        
    '''
    Creates article extractor for each player and returns articles
    '''
    def get_players(self):
        site = self.get_website();
        team_with_player_names = self.get_player_names(site)
        articles_dict = {}
        
        for team in team_with_player_names:
            player_article = {}
            for player in team_with_player_names[team]:
                player_article[player] = self.get_articles(player)
            
            articles_dict[team] = player_article
        return articles_dict
    
    '''
    Uses gamepedia for event information
    Returns main webpage for event
    '''
    def get_website(self):
        for site in googlesearch.search((self.event_name + 'gamepedia'), tld="com", num=1, start=0, stop=1, pause=2):
            return site
        
    '''
    Returns individual players seperated by team
    '''
    def get_player_names(self, site):        
        html = self.get_roster_site(site)
        soup = BeautifulSoup(html, "lxml")
  
        team_with_player_name = {}
        
        team_names = soup.find_all("span", {"class":"teamLongTitle"})        
        all_team_table = soup.find_all("table", {"class":"prettytable"})
        players = []
        
        # Go through each table
        for team_table, team_name in zip(all_team_table, team_names):            
            data = []
            # Seperate by row / column for player name
            rows = team_table.find_all("tr")
            
            for row in rows:
                # Don't include the coach
                if(row.find("img", {"alt":"CoachLanePick.png"})):
                    continue
                    
                cols = row.find_all("td")
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
            
            # New table of just player names
            player_names = [player[0] for player in data if len(player) == 2]

            team_with_player_name[team_name.text] = player_names
        
            players += player_names
        
        #return players
        return team_with_player_name
    
    '''
    Get articles for player
    '''
    def get_articles(self, name):
        try:
            article_extractor = ArticleExtractor(name, self.event_game)
            sites = article_extractor.get_websites()
            sources = [article_extractor.parse_websites(site) for site in sites]
        except:
            sources = ["Cannot Find Player"]
        return sources
    
    '''
    Get site with player rosters
    Checks for site that do not follow convention
    '''
    def get_roster_site(self, site):
        # League events
        if self.event_game == "league of legends":
            # LoL 2017 worlds - main event and playin event
            if '2017' in self.event_name.lower() and 'world' in self.event_name.lower():
                site = site + "/Main_Event/Team_Rosters"
            else:
                site = site + "/Team_Rosters"
        
        return request.urlopen(site).read().decode('utf8')
        