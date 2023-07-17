#examples/python/read_file.py
#reads a file with numpy.genfromtxt

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as colors

fname="data.txt"  #input the filename as a string

M1, M2 = np.genfromtxt(fname,dtype="float", \
comments="#", usecols=(3,4), unpack=True)

plt.scatter(M1, M2,s=0.001, color='green')


plt.hist2d(M1,M2,bins=250,norm=colors.LogNorm())
cbar = plt.colorbar()
cbar.set_label('Number of BBHs per cell')

