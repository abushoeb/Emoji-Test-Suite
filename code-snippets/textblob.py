# import library
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# load data
doc = TextBlob("Tweet goes here")

# tokenization
print(doc.tokens)

# pos tagging 
print(doc.tags)

# sentiment analysis with PatternAnalyzer
print(doc.sentiment)

# sentiment analysis with NaiveBayesAnalyzer
print(TextBlob("Tweet goes here", analyzer=NaiveBayesAnalyzer()).sentiment)