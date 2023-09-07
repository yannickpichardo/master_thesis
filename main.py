import numpy as np
import pandas as pd

#Create small function that will be used to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)
#Create unit test for distance function
assert distance(0, 0, 1, 1) == np.sqrt(2)
assert distance(0, 0, 0, 0) == 0

print(distance(0,0,1,1))
