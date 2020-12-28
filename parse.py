# Returns a list of paragraphs, stitching together multi-line paragraphs in judgment text by counting paragraph numbers.
def parse_lines(lines):
    output = []
    para = ""
    counter = 2
    in_num=False
    
    for line in lines:
        
        #remove multi-line paragraphs
        if line.split()[0] == str(counter): 
            index = len(str(counter-1))
            para = para[index+1:] #remove paragraph numbers
            para = para.lstrip()

            #remove footnote markers (up to 2 digits)
            new_para=''
            for i, char in enumerate(para):
                if char.isdigit() and in_num==False:
                    
                    if i==len(para)-2 or (para [i-1]=='.' and para[i+1].isdigit()): #end of para
                        in_num=True
                        
                    #middle of para
                    elif (i+2) < len(para):
                        if para[i-1]=='.' and para[i+2].isupper():  #single digit
                            in_num=True
                        elif para[i-1]=='.' and (para[i+3].isupper() or para[i+2]=='\n'): #double digit first num
                            in_num=True
                        else:
                            new_para+=char
                    
                    else:
                        new_para+=char      

                elif in_num==True and char!=' ':
                    continue
                    
                elif char ==' ' and in_num==True:
                    in_num=False
                    new_para+=' '

                else:
                    new_para+=char              
                    
            output.append(new_para)
            para = ""
            counter += 1  
            
        para += line + " "         # The paragraphs are formatted such that spaces are omitted before the newline. We reinsert them here to avoid joining the last word of the current line with the first word of the next line
        
        if line.split()[0] == "1":  # Reached end of case, start new case
            counter = 2
        
    output.append(para)
    return output
    
