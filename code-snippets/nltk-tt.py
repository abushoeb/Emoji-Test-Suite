# import library
import nltk
from nltk.tokenize.casual import TweetTokenizer

# load data
doc = "Tweet goes here"

t = TweetTokenizer()
# t = TweetTokenizer(strip_handles=True, reduce_len=True)

# tokenization
print(t.tokenize(doc))

# pos tagging
print(nltk.pos_tag(tokens))
