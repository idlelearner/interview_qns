n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m

print a

y = [[0]*4 for _ in range(3)]
print y
y[2][3] = 1
print y

tranpose = zip(*y)
print tranpose

from array import array
x = [3, 6, 9, 12, 1, 3]

s = set(x)
print s
