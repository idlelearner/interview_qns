# https://www.coderbyte.com/algorithm/find-duplicates-in-array-linear-time-v1
def find_duplicates(arr):
    count_map = {}
    for v in arr:
        if count_map.get(v):
            count_map[v]=count_map[v]+1
        else:
            count_map[v]=1
    for k,v in count_map.items():
        if v>1:
            print k,

if __name__=='__main__':
    find_duplicates([1,4,2,3,6,1,3,4])