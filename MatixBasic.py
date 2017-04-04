import numpy as np
x = np.array([1,5,2])
y = np.array([7,4,1])
print (x + y)
print (x * y)
print (x - y)
print (x / y)
print (x % y)


x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )
print(x * y)

x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
print(x * y)
