from sentencizers.sentencizer_baseline import sentencizer_baseline

# IMPORT YOUR TESTING FUNCTION HERE
# -----------------------------------------------------------
from sentencizers.my_sentencizer import my_sentencizer
# -----------------------------------------------------------

data = "./data/data_tiny.txt"
test = "./data/data_tiny_test.txt"

# generate list of sentences from manually delineated data 
lines = []
with open(test, encoding="utf8") as f:
  lines = [line.rstrip() for line in f]

test_paras = []
para = []
for line in lines:
  if line.strip() == "":
    test_paras.append(para)
    para = []
  else:
    para.append(line)
test_paras.append(para)


# process raw input data
lines = []
with open(data, encoding="utf8") as f:
  lines = [line.rstrip() for line in f]

data_paras = lines    # placeholder assumption, will need to add more processing for multiline quotes 

# apply baseline_sentencizer
data_paras_baseline = []
for para in data_paras:
  sentence = sentencizer_baseline(para)
  data_paras_baseline.append(sentence)

# apply sentencizer under test
data_paras_test = []
for para in data_paras:
  sentence = my_sentencizer(para)     # CHANGE THIS
  data_paras_test.append(sentence)


# compare correct data vs raw input data
# this is just a basic heuristic - can definitely be improved (see document for details)

# get expected number of sentences 
expected = 0 
for para in test_paras:
  for sentence in para:
    expected += 1

# check accuracy of baseline sentencizer
correct_baseline = 0
actual_baseline = 0
for i in range(len(data_paras_baseline)):
  for sentence in data_paras_baseline[i]:
    if sentence in test_paras[i]:
      correct_baseline += 1
  actual_baseline += 1

# check accuracy of sentencizer under test 
correct_test = 0
actual_test = 0
for i in range(len(data_paras_test)):
  for sentence in data_paras_test[i]:
    if sentence in test_paras[i]:
      correct_test += 1
  actual_test += 1

# Display results
print(f"RESULTS (baseline values in parentheses): \n\
  Expected number of sentences: {expected}; \n\
  Number of sentences identified: {actual_test} ({actual_baseline}); \n\
  Correctly identified: {correct_test} ({correct_baseline}); \n\
  Accuracy: {correct_test / expected :.2f} ({correct_baseline / expected :.2f})\
")