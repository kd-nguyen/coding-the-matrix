import sys
sys.path.insert(0, r'C:\Projects\coding-the-matrix\Data')

import numpy as np
from vec import *
from GF2 import *
from mat import *
from matutil import *

def button_vectors(n):
    D = {(i,j) for i in range(n) for j in range(n)}
    vecdict={(i,j):Vec(D,dict([((x,j),one) for x in range(max(i-1,0), min(i+2,n))]
    +[((i,y),one) for y in range(max(j-1,0), min(j+2,n))]))
    for (i,j) in D}
    return vecdict

B = coldict2mat(button_vectors(2))
print(B.f)

