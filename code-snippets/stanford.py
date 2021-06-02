# import library
import stanza

# setup pipeline
stanza.download('en', processors='tokenize,pos')
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos')

# load data
doc = nlp("Tweet goes here")

# tokenization
print([word.text for sent in doc.sentences for word in sent.words])

# pos tagging 
print([(word.text,word.pos) for sent in doc.sentences for word in sent.words])



