from scipy import spatial

import numpy as np

A = np.random.random((10,2))*100

#A

pt = [6, 30]  # <-- the point to find

A[spatial.KDTree(A).query(pt)[1]] # <-- the nearest point 
#array([  8.45828909,  30.18426696])

#how it works!
distance,index = spatial.KDTree(A).query(pt)

print distance # <-- The distances to the nearest neighbors

print index # <-- The locations of the neighbors


#then 
#A[index]
#array([  8.45828909,  30.18426696])