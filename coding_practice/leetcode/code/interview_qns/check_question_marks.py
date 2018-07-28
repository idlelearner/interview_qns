def QuestionsMarks(str): 
    # code goes here 
    stck = list()
    no_of_qm = 0
    for v in str:
        if v.isdigit():
            if no_of_qm == 3:
                while stck:
                    cur_val = stck.pop()
                    if cur_val == "?":
                        no_of_qm-=1
                    if cur_val.isdigit() and cur_val + v == 10:
                        return "true"
                no_of_qm = 0
            elif no_of_qm > 3:
                stck = list()
                stck.append(v)
            else:
                stck.append(v)
                
        if v == "?":
            no_of_qm+=1
            stck.append(v)
        
    return "false"
    
# keep this function call here  
print QuestionsMarks("acc?7??sss?3rr1??????5")