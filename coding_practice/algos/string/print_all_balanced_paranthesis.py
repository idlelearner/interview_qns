# https://www.coderbyte.com/algorithm/generate-balanced-bracket-combinations
def generate_paranthesis(open_count, close_count, paran_s, n):
    if close_count == n/2:
        print paran_s
    
    if open_count < n/2:
        generate_paranthesis(open_count+1, close_count, paran_s+"(", n)
    if close_count < n/2 and close_count<open_count:
        generate_paranthesis(open_count, close_count+1, paran_s+")", n)

def print_paranthesis(n):
    if n%2 == 1:
        print 'Cannot generate balanced paranthesis for odd lengths'
    else:
        generate_paranthesis(0,0,"", n)

if __name__=='__main__':
    print_paranthesis(2)
    print_paranthesis(3)
    print_paranthesis(4)
    print_paranthesis(6)

