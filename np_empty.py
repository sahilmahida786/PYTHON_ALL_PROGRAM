#   np.empty((rows,coulumns),dtype = int /str /bool /floor /etc)

import numpy as np
print(np.__version__)  #We are check version


# Example of ones    [1]      ( DATA TYPE BOOL = TRUE )
x = np.ones((4)) # columns
y = np.ones((4,5)) # rows and columns
z = np.ones((4,6),dtype = str) #We are Add the Data type (str)
print(x)
print(y)
print(z)



# Example of ZEROS  [0]      ( DATA TYPE BOOL = FALSE )

x = np.zeros((4)) # columns
y = np.zeros((4,6)) # rows and columns
z = np.zeros((4,9),dtype=int) # We are Add the Data type (int)
print(x)
print(y)
print(z)



# Lets we are try input type:
a = int(input ("Enter number of rows")) # Enter number of rows
b = int(input ("Enter number of columns")) # Enter number of coulumns
c = np.ones((a,b),dtype=int) 
print(c)