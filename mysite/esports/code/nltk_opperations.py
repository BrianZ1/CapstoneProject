# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:09:00 2018

@author: brian
"""

from nltk import Text, FreqDist, SnowballStemmer, pos_tag

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def to_nltk_text(text):
    return Text(text)

def get_sentance_tokens(text):
    return sent_tokenize(text)

def get_word_tokens(text):
    return word_tokenize(text)

def search_word(text, search):
    nltk_text = to_nltk_text(text)
    return nltk_text.concordance(search)

def get_word_frequency(word_tokens, search):
    nltk_text = to_nltk_text(word_tokens)
    return FreqDist(nltk_text)[search]

def get_stopwords():
    return set(stopwords.words('english'))

def get_stemmed_words(text):
    porter = SnowballStemmer("english")
    return [porter.stem(t) for t in text]

def get_pos_tag(word):
    return pos_tag([word])[0][1]