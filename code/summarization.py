# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:30:20 2018

@author: brian
"""

import nltk_opperations

'''
Convert the article from a list to a string
'''
def list_to_string(article):
    return ''.join(str(text) for text in article)

class Summarization:
    
    '''
    Main function for text summarizer
    '''    
    def summarize_text(self, article):
        string_text = list_to_string(article) 
        sentence_token_text = nltk_opperations.get_sentance_tokens(string_text)
        word_token_text = nltk_opperations.get_word_tokens(string_text)

        print(nltk_opperations.get_stemmed_words(word_token_text))
        
        return None

