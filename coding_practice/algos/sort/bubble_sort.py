def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

if __name__=='__main__':
    print bubble_sort([3,6,1,2,9])