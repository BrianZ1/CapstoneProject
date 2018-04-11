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
    def __init__(self, name, game, num_articles=2, start=None, end=None):
        self.player_name = name
        self.game_name = game
        self.num_articles = num_articles
        self.start_date = start
        self.end_date = end
        
        if start != None and end != None:
            start = start.replace('-','/')
            start = start[5:] + '/' + start[:4]
            self.start_date = start
            
            end = end.replace('-','/')
            end = end[5:] + '/' + end[:4]
            self.end_date = end
        #print("Looking up articles for player: " + self.player_name)

    '''
    Uses google api to get a list of sites
    '''
    def get_websites(self):
        search = " \" " + self.player_name + " \"\" " + self.game_name + " \" " + " player articles"
        
        if self.start_date == None and self.end_date == None: 
            return [site for site in 
                    googlesearch.search(search, num = self.num_articles,
                                        stop=self.num_articles, tpe='nws',
                                        only_standard=True)]
        else:
            time_range ='cdr:1,cd_min:' + self.start_date + ',cd_max:' + self.end_date
            return [site for site in 
                    googlesearch.search(search, num = self.num_articles,
                                        stop=self.num_articles, tpe='nws',
                                        tbs=time_range, only_standard=True)]

    '''
    Uses beautiful soup to parse given url.
    '''
    def parse_websites(self, url):  
        paragraph = []

        html = request.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
                
        for br in soup.find_all("br"):
            br.replace_with(" ")
            
        for p in soup.find_all('p'):
            if "Sort comment" in p.text or "PRIVACY POLICY" in p.text or "cookies" in p.text:
                continue
            paragraph.append(p.text.strip())

        return paragraph

class EventSeperator:
    '''
    Init class with event name and game to search
    '''
    def __init__(self, name, game, number_articles = 1):
        self.event_name = name
        self.event_game = game
        self.number_articles = number_articles
        #print("Looking up players for event: " + self.event_name)

    '''
    Uses liquipedia for event information on players / teams
    Returns main webpage for event
    '''
    def get_website(self):
        for site in googlesearch.search(self.event_name + ' liquipedia'):
            return site, self.get_event_time_period(site)

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
                
            if team_name:    
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
    
    '''
    Get event name
    '''
    def get_event_name(self):
        html = request.urlopen(self.get_website()[0]).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
        event_name = soup.find("h1", {"id": "firstHeading"})
        return event_name.text.strip()
    
    '''
    Get start and end dates for event
    '''
    def get_event_time_period(self, site):
        html = request.urlopen(site).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")
    
        info_box = soup.find_all("div", {"class": "infobox-cell-2"})
        
        for element in info_box:
            if element.text == "Start Date:":
                start_date = element.findNext('div').text
    
            if element.text == "End Date:":
                end_date = element.findNext('div').text
                
        return start_date, end_date
        
