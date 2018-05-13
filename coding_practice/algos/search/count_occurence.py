# count occurence in a elmt in a list
def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])

if __name__=='__main__':
     print count_occurrences([3,5,1,2,6,5,3],5)
     print count_occurrences([3,5,1,2,6,5,3],0)
