# Returns a list of paragraphs, stitching together multi-line paragraphs in judgment text by counting paragraph numbers.
def parse_lines(lines):
  output = []
  para = ""
  counter = 2
  for line in lines:
    if line.split()[0] == str(counter):
      output.append(para)
      para = ""
      counter += 1
    para += line + " "    # The paragraphs are formatted such that spaces are omitted before the newline. We reinsert them here to avoid joining the last word of the current line with the first word of the next line
  output.append(para)
  return output