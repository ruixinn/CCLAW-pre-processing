import spacy

def sentencizer_baseline(paragraph):
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(paragraph)
  sentences = list(doc.sents)
  return [sentence.text for sentence in sentences]