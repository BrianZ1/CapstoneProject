# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:30:20 2018

@author: brian
"""

import string
from word_probability import WordProbability
from naive_bayes_classifier import NaiveBayesClassifier

'''
Convert the article from a list to a string
'''
def list_to_string(article):
    return ' '.join(str(text) for text in article)

def remove_punctuation(text):
    punctuation = set(string.punctuation)
    return text.translate(dict.fromkeys(punctuation))

def word_in_string(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

class Summarization:

    def __init__(self, length):
        self.summary_length = length

    '''
    Main function for text summarizer
        start = timer()
        end = timer()
        print(end - start)
    '''
    def summarize_text(self, sites, articles):   
        if(len(articles) < 1):
            return ["Not enought information about player"]
        
        summary_methods = NaiveBayesClassifier()
    
        return summary_methods.get_summary(sites, articles, self.summary_length)
