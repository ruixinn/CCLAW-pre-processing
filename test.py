import spacy
from pysbd.utils import PySBDFactory

data = "data1.txt"
new_file=''
in_num = False


with open(data) as file:
    text = file.read()
    
    #conbine multiline quotes
    for i, char in enumerate(text[:-1]):
        if char =='\n':
            if text[i+1].islower():
                new_file += ' '
            else:
                new_file +=char
        
        
        elif char.isdigit() and in_num==False:
            
            #remove para numbers
            if text[i-1]=='\n': 
                in_num=True
                
            #remove footnote markers 
            elif (text[i-1]=='.' and text[i+2].isupper()) or (text[i-1]=='.' and text[i+1]=='\n'):  #single digit
                in_num=True
            elif text[i-1]=='.' and (text[i+3].isupper() or text[i+2]=='\n'): #double digit first num
                in_num=True
            else:
                new_file+=char
        
        elif (char ==' ' or char =='\n') and in_num==True:
            in_num=False
            new_file+=' '
         
        elif in_num==False:
            new_file+=char


new_file=new_file.replace('\n',' ')

def sentencizer_baseline(para):
    nlp= spacy.blank('en')
    nlp.add_pipe(PySBDFactory(nlp))

    doc = nlp(para)
    sentences = list(doc.sents)
    
    return [sentence.text for sentence in sentences]


for sentence in sentencizer_baseline(new_file):
    sentence = sentence.strip(' ')
    if sentence!= '':
        sentences.append(sentence)


