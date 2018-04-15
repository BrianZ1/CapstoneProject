# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:30:20 2018

@author: brian
"""

#from word_probability import WordProbability
from esports.code.naive_bayes_classifier import NaiveBayesClassifier

class Summarization:

    def __init__(self):
        self.summary_length = 5

    '''
    Main function for text summarizer
    '''
    def summarize_text(self, sites, articles):   
        if(len(articles) < 1):
            return ["Not enought information about player"]
        
        summary_methods = NaiveBayesClassifier()
    
        return summary_methods.get_summary(sites, articles)
