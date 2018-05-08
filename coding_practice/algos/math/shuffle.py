from copy import deepcopy
from random import randint

# shuffle the given list
# uses https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst

if __name__ == '__main__':
    print shuffle([1,2,3,4,5])
