from naive_bayes_classifier import NaiveBayesClassifier
import articles
import os

def list_to_string(article):
    return ''.join(str(text) for text in article)

def main():
    print("Navie Bayes Demo\n")

    nbc = NaiveBayesClassifier()
    
    sites = ["https://www.theplayerstribune.com/doublelift-league-of-legends-everyone-else-is-trash/"]
    article_extractor = articles.ArticleExtractor('doublelift', 'league of legends', 5)
    #sites = article_extractor.get_websites()
    article = [article_extractor.parse_websites(site) for site in sites]
    
    string_text = list_to_string(article)
    string_text = string_text.replace("', '", ' ')
    string_text = string_text.replace('", "', ' ')
    
    summary = nbc.get_summary(string_text, 5)
    
    print("Summary:")
    for sentence in summary:
        print(u'\u2022 ' + sentence.lstrip("[]1234567890',.\" "))
        
main()

os.system("pause")