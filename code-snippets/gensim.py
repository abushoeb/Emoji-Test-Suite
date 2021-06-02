# import library
import gensim

# load data
doc = "Tweet goes here"

# tokenization
print(list(gensim.utils.tokenize(doc)))

# pos tagging  
print(doc.parse())