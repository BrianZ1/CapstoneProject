import nltk_opperations
from pickle import load, dump
import nltk
from PyRouge.pyrouge import Rouge
import string

'''
Text summarization using a naive bayes classifier
'''
class NaiveBayesClassifier():

    '''
    Init class for classifier
    '''
    def __init__(self):
        self.clasifier = load_classifier()
    
    '''
    Main function to get summary
    '''
    def get_summary(self, text, summary_length):
        sentence_dict = self.calculate_sentence_score(text)
        return self.choose_best_sentences(sentence_dict) 
    
    '''
    Gives a score to each sentence in a text
    Use the classifer
    '''
    def calculate_sentence_score(self, text):
        sentence_dict = {}
        
        sentence_tokens = nltk_opperations.sent_tokenize(text)
 
        for sentence in sentence_tokens:
            distribution = self.clasifier.prob_classify(get_features(sentence, clean_article_sites(text)))
            sentence_dict[sentence] = distribution.prob("yes")
                
        return sentence_dict

    '''
    Chooses the best scoring sentences for the summary
    '''
    def choose_best_sentences(self, sentence_dict):
        return sorted(sentence_dict, key=sentence_dict.get, reverse=True)[:5]
    
'''*******************************************************
                Needed for both
*******************************************************'''   
def get_features(sentence, article):
    features = {}
    captial_count = 0
    word_frequency = 0
    number_count = 0
    adjective_count = 0
    
    word_tokens = nltk_opperations.get_word_tokens(sentence)
    stop_words_list = nltk_opperations.get_stopwords()
    
    word_list = [word for word in word_tokens 
                 if word not in stop_words_list 
                 and word not in string.punctuation]
    
    set(word_list)
    set(article)
    
    features['sentence_length'] = len(sentence)
    features['num_words'] = len(word_list)
    
    for word in word_list:
        
        if word.isupper():
            captial_count += 1
            
        if word.isnumeric():
            number_count += 1
            
        if nltk_opperations.get_pos_tag(word) == 'JJ':
            adjective_count += 1
            
        word_frequency += nltk_opperations.get_word_frequency(article, word)
            
    features['capital_words'] = captial_count
    features['numbers'] = number_count
    features['adjective_count'] = adjective_count
    
    try:
        features['word_freq'] = word_frequency / len(word_list)
    except:
        features['word_freq'] = 0

    return features
    
def list_to_string(article):
    return ' '.join(str(text) for text in article)

def load_classifier():
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = load(classifier_f)
    classifier_f.close()
    return classifier  

def clean_article_sites(article):
    stop_words_list = nltk_opperations.get_stopwords()
    sentence_token_text = nltk_opperations.get_sentance_tokens(article)

    clean_article = []
    for sent in sentence_token_text:
        word_token_text = nltk_opperations.get_word_tokens(sent)
        for word in word_token_text:
            if word not in stop_words_list and word not in string.punctuation:
                clean_article.append(word.lower())
    
    return clean_article
   
'''*******************************************************
                Training the classifier
*******************************************************'''    
def save_classifier(classifier):
    save_classifier = open("naivebayes.pickle","wb")
    dump(classifier, save_classifier)
    save_classifier.close()

def get_dataset():
    stories_f = open('cnn_dataset.pkl', 'rb')
    stories = load(stories_f)
    stories_f.close()
    return stories

def save_labeled_dataset(dataset):
    labeled_dataset = open("labeled_cnn_dataset.pkl", "wb")
    dump(dataset, labeled_dataset)
    labeled_dataset.close()
    
def load_labeled_dataset():
    labeled_dataset_f = open("labeled_cnn_dataset.pkl", "rb")
    labeled_dataset = load(labeled_dataset_f)
    labeled_dataset_f.close()
    return labeled_dataset

def read_dataset():
    dataset = {}
    r = Rouge()
    threshold = .70
    stories = get_dataset()
    
    for i in range(0, 2000):
        labeled_articles = set()
        story = stories[i]['story']
        highlights = stories[i]['highlights']
        
        for sent in story:
            for highlight in highlights:
                [precision, recall, f_score] = r.rouge_l(sent, highlight)
                
                if f_score > threshold:
                    labeled_articles.add((sent, 'yes'))
                else:
                    labeled_articles.add((sent, 'no'))

        dataset[i] = labeled_articles
        
    return dataset

def clean_article(article):
    stop_words_list = nltk_opperations.get_stopwords()
    story = article['story']
    clean_article = []
    for sent in story:
        word_token_text = nltk_opperations.get_word_tokens(sent)
        for word in word_token_text:
            if word not in stop_words_list and word not in string.punctuation:
                clean_article.append(word.lower())
    
    return clean_article
    
#def main():
    #labeled_articles = load_labeled_dataset()
    #full_articles = get_dataset()
    #featuresets = [(get_features(sentence, clean_article(full_articles[article])), label)
    #                for article in labeled_articles 
    #                for (sentence, label) in labeled_articles[article]]
    #featuresets = [(get_features(sentence, clean_article(full_articles[0])), label) for (sentence, label) in labeled_articles[0]]
    #train_set, test_set = featuresets, featuresets
    #classifier = nltk.NaiveBayesClassifier.train(train_set)
    #
    ##print(train_set)
    #print(nltk.classify.accuracy(classifier, test_set))
    #print(classifier.show_most_informative_features(30))
    #save_classifier(classifier)         
 
#main()
