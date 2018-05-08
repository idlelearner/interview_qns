a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# slicing examples
print a[-4:]
print a[:4]
print a[-3:3]

# list comprehension
sqrs = [x**2 for x in a]
print sqrs

matrix = [[1,2,3],[4,5,6],[7,8,9]]
f = [x for row in matrix for x in row]
print f

# for else block
for i in range(3):
    print 'Running - %s' % i
    if i==1:
        break
else:
    print "In else"

# Example for else excecution
v = []
for i in v:
    print 'Running - %s' % i
    if i==1:
        break
else:
    print "In else"

'''
# example else with try
def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key] # May raise KeyError
'''

# sorting based on priority for a group
def sort_values(num, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1,x
    num.sort(key=helper)

print "Sorting based on group priority"
num = [1,2,3,4,5,6,7,8,9]
group = [2,4,6]
sort_values(num, group)
print num