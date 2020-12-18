data = "data1.txt" #input data file name

with open(data) as file:
    text = file.read().replace('\n', ' ') #doesn't work lol

import spacy
nlp = spacy.load('en_core_web_sm') #lg
                
doc = nlp(text)
sentences = list(doc.sents)
for sentence in sentences:
        print(sentence)
        
## RL's attempt
import spacy # haven't really figured out how to use spacy yet
 
with open("./data/data.txt", 'r') as f:
    NUMBERS = '1234567890'
    paragraphs = []
    sentences = []
## to separate paragraphs
    for line in f:
        new = line.rstrip('\n')
        if new[0] in NUMBERS:
            new = new.strip(new[0])
            paragraphs.append(new)      
## to split sentences in each paragraph
    for para in paragraphs:
        sentence = para.split('.')
        sentences.append(sentence)
        print(sentence)
