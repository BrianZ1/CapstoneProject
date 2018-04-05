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
    def __init__(self, name, game, bullet_points=5):
        self.player_name = name
        self.game_name = game
        self.number_of_bullet_points = bullet_points
        #print("Looking up articles for player: " + self.player_name)

    '''
    Uses google api to get a list of sites
    '''
    def get_websites(self):
        return [site for site in 
                googlesearch.search(
                        " \" " + self.player_name + " \"\" " + self.game_name + " \" " + " player articles",
                                        num=2, stop=2, tpe='nws',
                                        only_standard=True)]

    '''
    Uses beautiful soup to parse given url.
    '''
    def parse_websites(self, url):  
        paragraph = []

        try:
            html = request.urlopen(url).read().decode('utf8')
            soup = BeautifulSoup(html, "lxml")

            for br in soup.find_all("br"):
                br.replace_with(" ")
                
            for p in soup.find_all('p'):
                if "Sort comment" in p.text or "PRIVACY POLICY" in p.text or "cookies" in p.text:
                    continue
                paragraph.append(p.text.strip())
        except:
            paragraph.append(" ")

        return paragraph


class EventSeperator:
    '''
    Init class with event name and game to search
    '''
    def __init__(self, name, game):
        self.event_name = name
        self.event_game = game
        self.number_of_bullet_points = 5
        #print("Looking up players for event: " + self.event_name)

    '''
    Uses liquipedia for event information on players / teams
    Returns main webpage for event
    '''
    def get_website(self):
        for site in googlesearch.search((self.event_name + 'liquipedia'), num=1, stop=1):
            return site

    '''
    Returns individual players and players seperated by team
    '''
    def get_player_team_names(self, site):
        html = request.urlopen(site).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
        team_with_player_name = {}

        teams_div = soup.find_all("div", {"class": "teamcard"})
        for team in teams_div:
            data = []
            
            team_name = team.find("a").text.strip()
            team_table = team.find("table")
            rows = team_table.find_all("tr")
            
            for row in rows:
                # Don't include the coach
                if(row.find("abbr", {"title": "Coach"})):
                    continue
                
                # Get the player name from each row
                cols = row.find("td")
                data.append(cols.text.strip())  
                
            team_with_player_name[team_name] = dict.fromkeys(data)
        
        return team_with_player_name

    '''
    Get articles for player
    '''
    def get_articles(self, player):
        article_extractor = ArticleExtractor(player, self.event_game)
        sites = article_extractor.get_websites()        
        source = [article_extractor.parse_websites(site) for site in sites]
        return source
