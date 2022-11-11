import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from numba import njit
@njit(fastmath=True, cache=True)
def mayor(a,b):
    c = False
    if a == b :
        c = a == b
    return c
    
    
    
mv = np.vectorize(mayor, otypes=[str])


a1 = np.array(['mar','hector', 'maria'])

a2 = np.array(['marcos','axel', 'maria'])

res = mv(a2,a1)
print(res)  