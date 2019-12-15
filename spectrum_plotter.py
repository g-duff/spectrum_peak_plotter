import os
import sys
import numpy as np

## Set wavelength range)
xi = 700
xf = 800

## We make a variable "root", which is the folder that you ##
## have draged and dropped this code into ##
root = os.getcwd()

## Our "data_files" variable is a list of all the .csv file names in the ##
## same folder that you dragged and dropped this code into. We sorted    ##
## names in order of earliest time to latest time. ##
data_files = (root+a for a in sorted(os.listdir(root)) if '.csv' in a)

## N is the number of file names in the directory ##
## We use it to estimate progress
N = len(os.listdir(root))

## Create an empty list which we will fill later. #
## We'll fill this list with the time at which each spectrum was taken ##
t = []

## Create another empty list to fill later. #
## We'll fill this list with the peak wavelength in every spectrum ##
peak_wl = []


## We load in each spectrum, one by one, and find the peak wavelength. ##
## We can do this in a for loop. ##
for index, selected_file in enumerate(data_files):

    ## "genfromtxt" loads the "selected_file" ##
    wl, i = np.genfromtxt(fname=selected_file, delimiter=';', skip_header=33,
                          skip_footer=1, unpack=True)

    ## Find intensity range, maximum intensity in that range
    ## and the wavelength to which that intensity value corresponds
    i1, i2 = np.argmin((wl-xi)**2), np.argmin((wl-xf)**2)
    peak_wl.append(wl[i1+np.argmax(i[i1:i2])])

    ## We pull the time stamp from inside name and convert to seconds ##
    ## This bit is horrible code and I know it
    with open(selected_file) as open_file:
        time_stamp = [open_file.readline() for i in range(4)]
    time_stamp = (time_stamp[3].split(';')[1])[:-1]+'0'

    ## Convert timestamp to minutes and add to our time list, t.
    hr, min, sec, ms = time_stamp[0:2], time_stamp[2:4] , time_stamp[4:6], time_stamp[6:]
    t_minutes = int(hr)*60+(int(min))+(int(sec)/60)
    t.append(t_minutes)
    print("Completion: " + str(int((index/N) *100))+'%', end='\r')

data = np.vstack((t-np.min(t), peak_wl)).T

np.savetxt(root+'peak_wavelengths.txt', data,
    delimiter='\t',
    header='time(min)\t\t\tpeak wavelength (nm)')
