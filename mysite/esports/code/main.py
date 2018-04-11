# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:46:58 2018

@author: brian
"""

from esports.code.articles import ArticleExtractor
from esports.code.summarization import Summarization

def player_search(query, game, num_articles, start, end):
    article_extractor = ArticleExtractor(query, game, num_articles, start, end)
    article_summarizer = Summarization()

    sites = article_extractor.get_websites()
    
    sources = [article_extractor.parse_websites(site) for site in sites]
    
    summary = article_summarizer.summarize_text(sites, sources)
    
    return summary