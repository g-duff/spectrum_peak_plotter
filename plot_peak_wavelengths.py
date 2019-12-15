# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import scipy.signal as sig
import os

root = os.getcwd()
root = '../2VFilter_1uMGlucose_Heat/'
t, rwl, iwl, cwl = np.genfromtxt(root+'peak_wavelengths.txt', skip_header=1, unpack=True)

plt.plot(t, rwl-1, 'C0.', markersize=3, label='None')
plt.plot(t, iwl, 'C1.', markersize=3, label='Linear')
plt.plot(t, cwl+1, 'C2.', markersize=3, label='Cubic')
plt.title('Comparing interpolation methods\n1nm offset between each')
plt.grid(True)
plt.xlabel('Time (minutes)')
plt.ylabel('Peak wavelength (nm)')
plt.legend(loc=0)
plt.savefig(root+'peak_wls.png')
plt.show()
