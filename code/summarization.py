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
    def summarize_text(self, article):
        string_text = list_to_string(article)
        string_text = string_text.replace("', '", ' ')
        string_text = string_text.replace('", "', ' ')
    
        if(len(string_text) < 1):
            return ["Not enought information about player"]
        
        #summary_methods = WordProbability()
        summary_methods = NaiveBayesClassifier()
    
        return summary_methods.get_summary(string_text, self.summary_length)
