import spacy

from pysbd.utils import PySBDFactory 
import spacy

def sentencizer_baseline(paragraph):
  nlp = spacy.blank('en')
  nlp.add_pipe(PySBDFactory(nlp))
  
  doc = nlp(paragraph)
  sentences = list(doc.sents)
  return [sentence.text for sentence in sentences]

# def sentencizer_baseline(paragraph):
#   nlp = spacy.load('en_core_web_sm')
#   doc = nlp(paragraph)
#   sentences = list(doc.sents)
#   return [sentence.text for sentence in sentences]