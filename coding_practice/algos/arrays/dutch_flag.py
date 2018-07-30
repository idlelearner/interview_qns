# https://www.coderbyte.com/algorithm/dutch-national-flag-sorting-problem
def dutch_flag(arr):
    i0, i = 0, 0
    i2 = len(arr)-1

    while i <= i2:
        if arr[i]==2:
            arr[i],arr[i2]=arr[i2],arr[i]
            i2-=1
        if arr[i]==0:
            arr[i0],arr[i] = arr[i], arr[i0]
            i0+=1
        i+=1

arr =  [2,2,2,0,0,0,1,1]
dutch_flag(arr)
print arr
