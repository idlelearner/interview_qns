x = [1,2,3,'a',5,6]
for i in (v for i, v in enumerate(x) if isinstance(v, int) and (v%2==1 or i%2==0)):
    print i


# to 100 using yield and therefore generator
 
# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1
 
    # An Infinite loop to generate squares 
    while True:
        yield i*i                
        i += 1  # Next execution resumes 
                # from this point     
 
# Driver code to test above generator 
# function
for num in nextSquare():
    if num > 100:
         break   
    print num 