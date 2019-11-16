import os
import sys
import numpy as np

## Set wavelength range)
xi = 700
xf = 800

## Root is defined as the directory in which this code sits. ##
root = os.getcwd()
## We use the operating system function "get current working directory". ##
## We want a list of all the spectrums that need to be analysed. We call ##
## this list, or array, data_files and it contains a sorted list of all  ##
## the spectrums. These are distinguished by their file extension (.csv).##
data_files = [a for a in sorted(os.listdir(root)) if '.csv' in a]
## We would like to know how many files are within data_files (the length). ##
N = len(data_files)
## Create a blank array to append the time stamps to ##
t = []
## Create a blank array to append the peak wavelengths to ##
peak_wl = []
## Now we want to individually load in every spectrum and analyse. We can do ##
## this in a for loop. ##
for index, selected_file in enumerate(data_files):
    ## Now we need to know the file path to this file, we use the operating ##
    ## system (os) function path.join to join our current path, and the file.##
    file = os.path.join(root, selected_file)
    ## Using numpy (a python library) we can load in the data values within ##
    ## the file. ##
    wl, i = np.genfromtxt(fname=file, delimiter=';', skip_header=33,
                          skip_footer=1, unpack=True)
    wavelength = np.arange(xi, xf + 1, 0.01)
    intensity = np.interp(x=wavelength, fp=i, xp=wl)
    peak = float(wavelength[np.argmax(intensity)])
    peak_wl.append(peak)
    ## We now pull the time stamp from the file name and convert to seconds ##
    time_stamp = (file.split('.')[0]).split('_')[::0-1]
    t.append((int(time_stamp[4])*24*60*60)+(int(time_stamp[3])*60*60)
            +(int(time_stamp[2])*60)+int(time_stamp[1])+(int(time_stamp[0])/1000))
    print(str(int((index/N) *100))+'%')
data = np.vstack((t, peak_wl)).T
print(data)
