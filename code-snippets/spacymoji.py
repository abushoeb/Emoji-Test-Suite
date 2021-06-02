# import library
import spacy
from spacymoji import Emoji

# load language model
nlp = spacy.load("en_core_web_sm")

# add emoji support to the pipe
emoji = Emoji(nlp, merge_spans=True)
nlp.add_pipe(emoji, first=True)

# load data
doc = nlp("Tweet goes here")

# tokenization
print([token.text for token in doc])

# pos tagging
print([(token.text,token.pos_, token.tag_) for token in doc])