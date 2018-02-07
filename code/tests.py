# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:37:04 2018

@author: brian
"""

# Testing article extractor
from articles import ArticleExtractor

articles = ArticleExtractor("doublelift", "league of legends")

article = articles.get_articles()

print(article)

## Testing summarization link
#from summarization import Summarization
#
#summarization = Summarization()
#
## Testing sentence tokenizer / make sure the articles are split correctly
#for a in article:
#    text = summarization.test(''.join(a))
#
#    for t in text:
#        print(t)
#
## Testing eventlookup
#from articles import ArticleExtractor
#from articles import EventSeperator
#
#event = EventSeperator('2017 Worlds Championship', 'League of Legends')
#
#info = event.get_players()
#
## Example for one team
#for player in info['Team SoloMid']:
#    print(player)
#    print(info['Team SoloMid'][player])
#    print("\n")
#
## Example for all teams
#for team in info:
#    for player in info[team]:
#        print(player)
#        print(info[team][player])
#        print("\n")
