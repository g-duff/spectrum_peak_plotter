import os
import sys
import numpy as np
from scipy.optimize import least_squares
from photonics import fano_residuals, fano
from matplotlib import pyplot as plt

## Set wavelength range)
wl1 = 730
wl2 = 740

## We make a variable "root", which is the folder that you ##
## have draged and dropped this code into ##
root = os.getcwd()

## Our "data_files" variable is a list of all the .csv file names in the ##
## same folder that you dragged and dropped this code into. We sorted    ##
## names in order of earliest time to latest time. ##
data_files = [a for a in sorted(os.listdir(root)) if '.csv' in a]

## N is the number of file names in the list called "data_files" ##
N = len(data_files)

## Create an empty list which we will fill later. #
## We'll fill this list with the time at which each spectrum was taken ##
t = []

## Create another empty list to fill later. #
## We'll fill this list with the peak wavelength in every spectrum ##
peak_wl = []
fit_wl = []

## We load in each spectrum, one by one, and find the peak wavelength. ##
## We can do this in a for loop. ##
for index, selected_file in enumerate(data_files):

    ## "genfromtxt" loads the "selected_file" ##
    wl, i = np.genfromtxt(fname=selected_file, delimiter=';', skip_header=33,
                          skip_footer=1, unpack=True)

    i1, i2 = np.argmin((wl-wl1)**2), np.argmin((wl-wl2)**2)

    wl = wl[i1:i2]
    i = i[i1:i2]

    ## We find the peak wavelength and append it to our "peak_wl" list
    peak = float(wl[np.argmax(i)])
    peak_wl.append(peak)

    ## Perform Fano fit
    popt = [peak, -4.97554893e+00,  2.41074476e-01, -4.26937633e-01, 6.76618253e-01]
    fano_fit = least_squares(fano_residuals, popt, args=(wl, i))
    fit_wl.append(fano_fit.x[0])

    ## We pull the time stamp from the file name and convert to seconds ##
    time_stamp = (selected_file.split('.')[0]).split('_')[::-1]
    t.append((int(time_stamp[4])*24*60*60)+(int(time_stamp[3])*60*60)
            +(int(time_stamp[2])*60)+int(time_stamp[1])+(int(time_stamp[0])/1000))
    print("Completion: " + str(int((index/N) *100))+'%', end='\r')

data = np.vstack((t, peak_wl)).T
plt.plot(t, peak_wl)
plt.plot(t, fit_wl)
plt.show()
