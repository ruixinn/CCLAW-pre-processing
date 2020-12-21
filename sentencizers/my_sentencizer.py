from pysbd.utils import PySBDFactory 
import spacy

# EDIT THIS FUNCTION
def my_sentencizer(paragraph):
  nlp = spacy.blank('en')
  nlp.add_pipe(PySBDFactory(nlp))
  
  doc = nlp(paragraph)
  sentences = list(doc.sents)
  return [sentence.text for sentence in sentences]