# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:37:04 2018

@author: brian
"""

# Testing article extractor
from articles import ArticleExtractor

articles = ArticleExtractor("doublelift")

article = articles.get_articles()

# Testing summarization link
from summarization import Summarization

summarization = Summarization()

# Testing sentence tokenizer / make sure the articles are split correctly
for a in article:
    text = summarization.test(''.join(a))
    
    for t in text:
        print(t)
        
# Testing eventlookup 
from articles import EventSeperator

event = EventSeperator('2017 Worlds', 'League of Legends')

# only gets teams so far, no list of players
print(event.get_players())