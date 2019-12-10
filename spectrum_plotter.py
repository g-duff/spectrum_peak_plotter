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

    ## We pull the time stamp from inside name and convert to seconds ##
    ## This bit is horrible code and I know it
    with open(selected_file) as open_file:
        time_stamp = [open_file.readline() for i in range(4)]
    time_stamp = time_stamp[3].split(';')[1]

    print(time_stamp)
    # print(time_stamp)
    # t.append((int(time_stamp[4])*24*60*60)+(int(time_stamp[3])*60*60)
    #         +(int(time_stamp[2])*60)+int(time_stamp[1])+(int(time_stamp[0])/1000))
    # print("Completion: " + str(int((index/N) *100))+'%', end='\r')

## Order the data from earliest to latest time

data = np.vstack((t, peak_wl)).T
print(data)
