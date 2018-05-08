# Return top n elements in the list
def max_n(lst, n):
    return sorted(lst, reverse=True)[:n]

if __name__ == '__main__':
    print max_n([2,4,1,2,9], 2)
    print max_n([5,10,2,3], 1)