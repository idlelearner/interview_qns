def insertInterval(arr, interval):
    if not arr:
        return [interval]
    result = []
    new_interval_present = False
    new_interval_st, new_interval_end = None, None

    for v in arr:
        print v
        if (v[0]<interval[0] and v[1]<interval[0]) or (v[0]>interval[1] and v[1]>interval[1]):
            if new_interval_present:
                result.append([new_interval_st, new_interval_end])
                new_interval_present = False
            result.append(v)
        else:
            new_interval_present = True
            new_interval_st = min(v[0], interval[0])
            new_interval_end = max(v[1], interval[1])

    if new_interval_present:
        result.append([new_interval_st, new_interval_end])
        
    if arr[len(arr)-1][1]<interval[0]:
        result.append([interval[0], interval[1]])

    return result


print insertInterval([[4,5],[10,15],[20,29],[35,40]], [12,43])