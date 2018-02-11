# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:09:00 2018

@author: brian
"""

from nltk import sent_tokenize, word_tokenize, Text, FreqDist, corpus, PorterStemmer

def to_nltk_text(text):
    return Text(text)

def get_sentance_tokens(text):    
    return sent_tokenize(text)

def get_word_tokens(text):
    return word_tokenize(text)

def search_word(text, search):
    nltk_text = to_nltk_text(text)  
    return nltk_text.concordance(search)

def get_word_frequency(text):
    nltk_text = to_nltk_text(text)
    return FreqDist(nltk_text)

def get_stopwords():
    return corpus.stopwords.words('english')

def get_stemmed_words(text):
    porter = PorterStemmer()
    return [porter.stem(t) for t in text]