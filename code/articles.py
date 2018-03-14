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
        self.number_of_bullet_points = 5
        self.include_gamepedia = True
        #print("Looking up articles for player: " + self.player_name)

    '''
    Uses google api to get a list of sites
    '''
    def get_websites(self):
        sites = []
        for site in googlesearch.search(self.player_name + self.game_name, tld="com", lang='en', num=1, start=0, stop=1, pause=2):
            if len(site) == 5:
                break;
            
            if '#' in site or 'youtube' in site or 'twitter' in site or 'facebook' in site or 'urbandictionary' in site:
                continue
                
            if self.include_gamepedia is False and 'gamepedia' in site:
                continue

            if 'gamepedia' in site:
                self.include_gamepedia = False

            if "com" in site:
                    
#                print("Adding site: " + site)
                sites.append(site)
        return sites

    '''
    Uses beautiful soup to parse given url.
    '''
    def parse_websites(self, url):
#        print("Parsing site: " + url)
        
        paragraph = []

        try:
            html = request.urlopen(url).read().decode('utf8')
            soup = BeautifulSoup(html, "lxml")

            for p in soup.find_all('p'):
                paragraph.append(p.text.strip())
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
        print("Looking up players for event: " + self.event_name)

    '''
    Uses gamepedia for event information
    Returns main webpage for event
    '''
    def get_website(self):
        for site in googlesearch.search((self.event_name + 'gamepedia'), tld="com", num=1, start=0, stop=1, pause=2):
            return site

    '''
    Returns individual players and players seperated by team
    '''
    def get_player_team_names(self, site):
        html = self.get_roster_site(site)
        soup = BeautifulSoup(html, "lxml")

        team_with_player_name = {}
        players = []

        team_names = soup.find_all("span", {"class": "mw-headline"})
        all_team_table = soup.find_all("table", {"class": "prettytable"})
        
        # Go through each table
        for team_table, team_name in zip(all_team_table, team_names):
#            print("\nFound team:" + str(team_name.text))
            data = []
            # Seperate by row / column for player name
            rows = team_table.find_all("tr")

            for row in rows:
                # Don't include the coach
                if(row.find("img", {"alt": "CoachLanePick.png"})):
                    continue

                cols = row.find_all("td")
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])

            # New table of just player names
            player_names = [player[0] for player in data if len(player) == 2]
#            print("Found players:" + str(player_names))
            
            #Keep tracks a list of players
            players += player_names
            
            team_with_player_name[team_name.text] = dict.fromkeys(player_names)

        # return players
        return team_with_player_name, players

    '''
    Get articles for player
    '''
    def get_articles(self, player):
        article_extractor = ArticleExtractor(player, self.event_game)
        sites = article_extractor.get_websites()        
        source = [article_extractor.parse_websites(site) for site in sites]
        return source
        
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
