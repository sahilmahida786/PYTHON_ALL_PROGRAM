# create 100 folders in os!

import os 

if (not os.path.exists("data")): #exits folder are also create.
    os.mkdir("data")# enter folder name.

for x in range(0, 100): # create 100 folder in  for loop.
    os.mkdir(f"data/Day {x+1}")
