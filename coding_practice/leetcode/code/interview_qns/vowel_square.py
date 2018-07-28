def VowelSquare(strArr): 
    res = ""
    # code goes here
    vowels = "aeiou"
    for i in xrange(0, len(strArr)-1):
        for j in xrange(0, len(strArr[0])-1):
            print "%s, %s, %s, %s" % (i,j,strArr[i][j],strArr[i][j] in vowels)
            print "%s, %s, %s, %s" % (i,j+1,strArr[i][j+1],strArr[i][j+1] in vowels)
            print "%s, %s, %s, %s" % (i+1,j,strArr[i+1][j],strArr[i+1][j] in vowels)
            print "%s, %s, %s, %s" % (i+1,j+1,strArr[i+1][j+1],strArr[i+1][j+1] in vowels)
            print "-"*50
            if (strArr[i][j] in vowels and \
                strArr[i+1][j] in vowels and \
                strArr[i][j+1] in vowels and \
                strArr[i+1][j+1] in vowels):
                return "%s-%s"%(i,j)
    
    return "not found"
    
# keep this function call here  
print VowelSquare(["abcd", "eikr", "oufj"])  