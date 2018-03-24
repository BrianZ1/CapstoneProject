import nltk_opperations
from pickle import load, dump
import nltk
from PyRouge.pyrouge import Rouge

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
            distribution = self.clasifier.prob_classify(get_features(sentence))
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
def get_features(sentence):
    features = {}
#    capitals = 0
#    numbers = 0
#    stop_words = 0
#    adjectives = 0
    
    features['sentence_length'] = len(sentence)
    
#    word_token_text = nltk_opperations.get_word_tokens(sentence)
#    stop_words_list = nltk_opperations.get_stopwords()
#    
#    for word in word_token_text:
#        if word[0].isupper():
#            capitals += 1
#            
#        if word.isdigit():
#            numbers += 1
#            
#        if word.lower() in stop_words_list:
#            stop_words += 1
#            
#        if nltk.pos_tag([word])[0][1]:
#            adjectives += 1
#        
#    features['capital_words'] = capitals
#    features['numbers'] = numbers
#    features['stop_words'] = stop_words
#    features['adjectives'] = adjectives

    return features
    
def list_to_string(article):
    return ''.join(str(text) for text in article)

def load_classifier():
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = load(classifier_f)
    classifier_f.close()
    return classifier  
   
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
    labeled_articles = set()
    r = Rouge()
    threshold = .70
    stories = get_dataset()
    
    for i in range(0, 2000):
        story = stories[i]['story']
        highlights = stories[i]['highlights']
        
        for sent in story:
            for highlight in highlights:
                [precision, recall, f_score] = r.rouge_l(sent, highlight)
                
                if f_score > threshold:
                    labeled_articles.add((sent, 'yes'))
                else:
                    labeled_articles.add((sent, 'no'))
    
    return labeled_articles
    
def main():
    labeled_articles = load_labeled_dataset()
    #random.shuffle(labeled_articles)
    featuresets = [(get_features(sentence), label) for (sentence, label) in labeled_articles]
    train_set, test_set = featuresets[40000:], featuresets[:20000]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    #print(train_set)
    #print(nltk.classify.accuracy(classifier, test_set))
    #save_classifier(classifier)         
 
#main()