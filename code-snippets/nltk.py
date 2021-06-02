# import library
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

# load data
doc = "Tweet goes here"

# tokenization
print(nltk.word_tokenize(doc))

# pos tagging 
print(nltk.pos_tag(tokens))

# sentiment analysis
vader = SentimentIntensityAnalyzer()
print(vader.polarity_scores(doc))