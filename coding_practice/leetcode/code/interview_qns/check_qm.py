def QuestionsMarks(str): 
    no_of_qm = 0
    f_no,s_no,f_pos,s_pos = 0, 0, 0, 0
    while j<len(str):
        i=j
        while not v[i].isdigit() and i<len(str):
            i+=1
        f_pos, f_no = i, int(v[i])

        while no_of_qm<3 and i<len(str):
            if v[i]=="?":
                no_of_qm+=1
            i+=1
        
        while not v[i].isdigit() and i<len(str):
            if v[i]=="?":
                break
            i+=1
        if 
        s_pos, s_no = i, int(v[i])




            

    return "false"
    
# keep this function call here  
print QuestionsMarks("acc?7??sss?3rr1??????5")