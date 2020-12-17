data = "data1.txt" #

with open(data) as file:
    text = file.read().replace('\n', ' ')

import spacy
nlp = spacy.load('en_core_web_sm') #lg
                
doc = nlp(text)
sentences = list(doc.sents)
for sentence in sentences:
        print(sentence)
