import nltk_opperations
from pickle import load, dumb
import nltk

'''
Text summarization using a naive bayes classifier
'''
class NaiveBayesClassifier():

    '''
    Init class for classifier
    '''
    def __init__(self, train=False):
        self.clasifier = load_classifier()
    
    '''
    Main function to get summary
    '''
    def get_summary(self, text, summary_length):

        pass 
    
        '''
    Gives a score to each sentence in a text
    Use the classifer
    '''
    def calculate_sentence_score(self):
        
        # for each sentence
        # dist = classifier.prob_classify(features())
        #print(list(dist.samples()))
        #print(dist.prob("Yes"))
        #print(dist.prob("No"))
        
        # return dict
        pass

    '''
    Chooses the best scoring sentences for the summary
    '''
    def choose_best_sentences(self):
        
        pass
   
    
'''*******************************************************
                Training the classifier
*******************************************************'''    
def save_classifier(classifier):
    save_classifier = open("naivebayes.pickle","wb")
    dump(classifier, save_classifier)
    save_classifier.close()
    
def load_classifier():
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = load(classifier_f)
    classifier_f.close()
    return classifier   

def get_dataset():
    stories = load(open('cnn_dataset.pkl', 'rb'))
    return stories

def get_labels():
    return ['yes', 'no']

def get_features(sentence):
    features = {}
    
    features['test'] = len(sentence)

    return features

def read_dataset():
    labeled_articles = []
    
    return labeled_articles

labeled_articles = read_dataset()
#random.shuffle(labeled_articles)
featuresets = [(get_features(sentence), label) for (sentence, label) in labeled_articles]
train_set, test_set = featuresets, featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set)

#print(nltk.classify.accuracy(classifier, test_set))
#save_classifier(classifier)         