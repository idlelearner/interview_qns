# https://www.coderbyte.com/algorithm/lucky-sevens
def lucky_sevens(arr):
    if len(arr) < 3:
        return False
    for i in range(len(arr)-2):
        if (arr[i] + arr[i+1] + arr[i+2]) == 7:
            return True

    return False

print lucky_sevens([2, 1, 5, 1, 0])
print lucky_sevens([1]*1000)