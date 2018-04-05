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