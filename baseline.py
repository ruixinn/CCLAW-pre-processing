from sentencizers.sentencizer_baseline import sentencizer_baseline

def apply_baseline(data_paras):
  data_paras_baseline = []
  for para in data_paras:
    sentence = sentencizer_baseline(para)
    data_paras_baseline.append(sentence)
  return data_paras_baseline


if __name__ == "__main__":
  from parse import parse_lines
  data = "./data/data_small.txt"
  test = "./data/data_small_test.txt"

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
  lines = []
  with open(data, encoding="utf8") as f:
    lines = [line.rstrip() for line in f]

  data_paras = parse_lines(lines)

  assert len(data_paras) == len(correct_paras), "Number of paragraphs in data and test files unequal."

  # apply baseline_sentencizer
  print("Applying baseline sentencizer...")
  data_paras_baseline = apply_baseline(data_paras)
  print("Completed baseline sentencizer")
  
  # get expected number of sentences 
  expected = 0 
  for para in correct_paras:
    expected += len(para)

  # check accuracy of baseline sentencizer
  correct_baseline = 0
  actual_baseline = 0

  for i in range(len(data_paras_baseline)):
    for sentence in data_paras_baseline[i]:
      if sentence in correct_paras[i]:
        correct_baseline += 1
      actual_baseline += 1 
  

  print(f"RESULTS (BASELINE): \n\
  Expected number of sentences: {expected}; \n\
  Number of sentences identified: {actual_baseline}; \n\
  Correctly identified: {correct_baseline}; \n\
  Accuracy: {correct_baseline / expected :.2f}\
")