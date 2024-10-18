#np.arange(start,end,step)

import numpy as np
x = np.arange(99) # arange means [0,1,2,3....98]
y = np.arange(0,30) # (start,end)
z = np.arange(0,30,3)# (start,end,step)
print(x)
print(y)
print(z)


# arr.reshape((rows,cols))
a = np.arange((16))     # 4 * 4 = 16
x = a.reshape((4,4))
print(x)


x = np.arange(1,100,2) # print 1 to 100 odd number:
print(x)

a = np.arange(1,100,2) 
y = a.reshape((10,5)) # 10 rows and 5 cols:
print(y)


# flatten() rows convert into cols
a = np.arange(1,100,2) 
x = a.flatten() #single  row and multiples cols
print(x)
