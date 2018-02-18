# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:30:20 2018

@author: brian
"""

import nltk_opperations
import string
import os

'''
Convert the article from a list to a string
'''
def list_to_string(article):
    return ''.join(str(text) for text in article)


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
    '''
    def summarize_text(self, article):
        string_text = list_to_string(article)
        string_text = string_text.replace("', '", ' ')
        string_text = string_text.replace('", "', ' ')
        sentence_token_text = nltk_opperations.get_sentance_tokens(string_text)
        word_token_text = nltk_opperations.get_word_tokens(string_text)

        wp = WordProbability()
        
#        print("\nCalculating word probability")
        word_dict = wp.calculate_word_probability(word_token_text)

        summary = []
        for i in range(self.summary_length):
            sentence_dict = wp.calculate_sentence_score(sentence_token_text, word_dict)
            best_sentence = wp.choose_best_sentences(sentence_dict, word_dict)
            summary.append(best_sentence) 
            word_dict = wp.update_weight(best_sentence, word_dict)
        return summary

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
            if word.lower() in nltk_opperations.get_stopwords():
                continue
            word_dict[word] = nltk_opperations.get_word_frequency(tokens, word) / len(tokens)

        return word_dict

    '''
    Gives a score to each sentence in a text
    Calculated as the average word probability of all words in the sentence
    '''
    def calculate_sentence_score(self, sentences, word_dict):
        sentence_dict = {}

        for sentence in sentences:
            score = 0
            word_list = nltk_opperations.get_word_tokens(sentence)

            for word in word_list:
                if word_dict.get(word):
                    score += word_dict[word]

            sentence_dict[sentence] = score / len(word_list)

        return sentence_dict

    '''
    Chooses the best scoring sentences for the summary
    '''
    def choose_best_sentences(self, sentence_dict, word_dict):
        highest_probability_word = sorted(word_dict, key=word_dict.get, reverse=True)[0]
        sentences_with_word = [sentence for sentence in sentence_dict if word_in_string(sentence, highest_probability_word)]
#        print("Highest probability word: " + highest_probability_word)

        best_score = 0
        best_sentence = ""

        for sentence in sentences_with_word:
            score = 0
            count = 0
            word_list = nltk_opperations.get_word_tokens(sentence)

            for word in word_list:                
                if word_dict.get(word):
                    count += 1
                    score += word_dict[word]

            if (score / count) > best_score:
                best_score = score
                best_sentence = sentence

        return best_sentence

    '''
    Update the weight for each word in the chosen sentence
    Calculated as new(wp) = old(wp) * old(wp)
    '''
    def update_weight(self, sentence, word_dict):
        word_list = nltk_opperations.get_word_tokens(sentence)

        for word in word_list:
            if word_dict.get(word):
                word_dict[word] = word_dict[word] * word_dict[word]

        return word_dict