import numpy as np
from numpy.linalg import solve

A=np.array([[0.,9.,5.],[5.,0.,0.],[2.,-1.,0.]])
b=np.array([2.,-2.,3.])
x=np.zeros(3,float)
x=solve(A,b)