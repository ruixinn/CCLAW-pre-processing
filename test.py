from baseline import apply_baseline
from parse import parse_lines

import spacy
from pysbd.utils import PySBDFactory


# IMPORT YOUR TESTING FUNCTION HERE
# -----------------------------------------------------------
from sentencizers.sentencizer_baseline import sentencizer_baseline
# -----------------------------------------------------------

data = "./data/data_small.txt"
test = "./data/data_small_test.txt"

# Disable this if you only want to run the sentencizer under test to save time
# -----------------------------------------------------------
APPLY_BASELINE = False
# -----------------------------------------------------------

# generate list of sentences from manually delineated data 
lines = []
with open(test, encoding="utf8") as f:
  lines = [line.rstrip() for line in f]

correct_paras = []
para = []
for line in lines:
  if line.strip() == "":
    correct_paras.append(para)
    para = []
  else:
    para.append(line)
correct_paras.append(para)


# process raw input data
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

# assert len(data_paras) == len(correct_paras), "Number of paragraphs in data and test files unequal."

# apply baseline_sentencizer
if APPLY_BASELINE:
  print("Applying baseline sentencizer...")
  data_paras_baseline = apply_baseline(new_file)
  print("Completed baseline sentencizer")

# apply sentencizer under test
print("Applying test sentencizer...")
data_paras_test = []
# for para in data_paras:
sentence = sentencizer_baseline(new_file)     # Change this if your sentencizer is in a different file 
# data_paras_test.append(sentence)

print("Completed test sentencizer")
print("Comparing results...")


# compare correct data vs raw input data
# this is just a basic heuristic - can definitely be improved (see document for details)

# get expected number of sentences 
expected = 0 
for para in correct_paras:
  expected += len(para)

# check accuracy of baseline sentencizer
correct_baseline = 0
actual_baseline = 0

if APPLY_BASELINE:
  for i in range(len(data_paras_baseline)):
    for sentence in data_paras_baseline[i]:
      if sentence in correct_paras[i]:
        correct_baseline += 1
      actual_baseline += 1

# check accuracy of sentencizer under test 
correct_test = 0
actual_test = 0

wrong_paragraphs = []
for i in range(len(data_paras_test)):
  for sentence in data_paras_test[i]:
    if sentence in correct_paras[i]:
      correct_test += 1
    else:
      if i not in wrong_paragraphs:
        wrong_paragraphs.append(i)
    actual_test += 1

# Display results
print(f"RESULTS (baseline values in parentheses): \n\
  Expected number of sentences: {expected}; \n\
  Number of sentences identified: {actual_test} ({actual_baseline}); \n\
  Correctly identified: {correct_test} ({correct_baseline}); \n\
  Accuracy: {correct_test / expected :.2f} ({correct_baseline / expected :.2f})\
")

# if input("Write wrong paragraphs to file? (y)") == "y":
if True:          # just a placeholder
  with open("./outputs/output.txt", "w", encoding="utf-8") as f:
    for i in wrong_paragraphs:
      f.write(f"EXPECTED: {'###'.join(correct_paras[i])}\n")
      f.write(f"ACTUAL:   {'###'.join(data_paras_test[i])}\n\n")
  print()
  print(f"{len(wrong_paragraphs)} wrong paragraphs written to ./outputs/output.txt")