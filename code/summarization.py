# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:30:20 2018

@author: brian
"""

import nltk_opperations
import string


'''
Convert the article from a list to a string
'''
def list_to_string(article):
    return ''.join(str(text) for text in article)


def remove_punctuation(text):
    punctuation = set(string.punctuation)
    return text.translate(dict.fromkeys(punctuation))


class Summarization:

    '''
    Main function for text summarizer
    '''
    def summarize_text(self, article):
        string_text = list_to_string(article).lower()
        sentence_token_text = nltk_opperations.get_sentance_tokens(string_text)
        word_token_text = nltk_opperations.get_word_tokens(string_text)

        wp = WordProbability()
        word_dict = wp.calculate_word_probability(word_token_text)

        return None
       
'''
Text summarization using word probability
'''
class WordProbability():

    '''
    Gives a score to each unique word in a text
    Calculated as word count / total number of words
    '''
    def calculate_word_probability(self, tokens):
        word_dict = {}
        unique_words = set(token for token in tokens if token.isalnum())

        for word in unique_words:
            word_dict[word] = nltk_opperations.get_word_frequency(tokens, word) / len(tokens)

        return word_dict

    '''
    Gives a score to each sentence in a text
    Calculated as the average word probability of all words in the sentence
    '''
    def calculate_sentence_score(self):
        return None

    '''
    Chooses the best scoring sentences for the summary
    '''
    def choose_best_sentences(self):
        return None

    '''
    Update the weight for each word in the chosen sentence
    Calculated as new(wp) = old(wp) * old(wp)
    '''
    def update_weight(self):
        return None
