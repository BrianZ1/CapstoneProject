# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:37:04 2018

@author: brian
"""
import articles
import summarization
#import os #os.system("PAUSE")

sites = ["https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/"]
article_extractor = articles.ArticleExtractor('doublelift', 'league of legends', 5)
sources = [article_extractor.parse_websites(site) for site in sites]

article_summarizer = summarization.Summarization()
sentences = article_summarizer.summarize_text(sources)
