data = "./data/data_small.txt"
test = "./data/data_small_test.txt"

from parse import parse_lines

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

data_paras = parse_lines(lines)

print(f"Number of lines in test = {len(test_paras)}")
print(f"Number of lines in data = {len(data_paras)}")