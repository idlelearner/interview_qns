for v in "abc1":
    print v.isdigit()

s = "abc2"
print s
l = list(s)
l[2] = "d"
print ''.join(l)

import random
print random.randint(0,3)
random.shuffle(l)
print l

# bisect
import bisect
a = [1,4,6,7]
print 'location where to insert'
print bisect.bisect(a, 5)
bisect.insort(a, 5)
print a