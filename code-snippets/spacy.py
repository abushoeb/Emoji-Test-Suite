# import library
import spacy

# load language model
nlp = spacy.load("en_core_web_sm")

# load data
doc = nlp("Tweet goes here")

# tokenization
print([token.text for token in doc])

# pos tagging 
print([(token.text,token.pos_, token.tag_) for token in doc])