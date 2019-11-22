import os
import sys
import numpy as np

## This program ...... blah blah

## Set wavelength range)
xi = 700
xf = 800

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


## We load in each spectrum, one by one, and find the peak wavelength. ## 
## We can do this in a for loop. ##
for index, selected_file in enumerate(data_files):
        
    ## "genfromtxt" loads the "selected_file" ##
    wl, i = np.genfromtxt(fname=selected_file, delimiter=';', skip_header=33,
                          skip_footer=1, unpack=True)
    
    wavelength = np.arange(xi, xf + 1, 0.01)
    intensity = np.interp(x=wavelength, fp=i, xp=wl)
    
    ## We find the peak wavelength and append it to our "peak_wl" list
    peak = float(wavelength[np.argmax(intensity)])
    peak_wl.append(peak)

    ## We pull the time stamp from the file name and convert to seconds ##
    time_stamp = (selected_file.split('.')[0]).split('_')[::-1]
    t.append((int(time_stamp[4])*24*60*60)+(int(time_stamp[3])*60*60)
            +(int(time_stamp[2])*60)+int(time_stamp[1])+(int(time_stamp[0])/1000))
    print("Completion: " + str(int((index/N) *100))+'%', end='\r')

data = np.vstack((t, peak_wl)).T
print(data)
