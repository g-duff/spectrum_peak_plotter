import os
import sys
import numpy as np

## We fit a "Fano lineshape" to the peak in the spectrum
## Python needs a Fano function, defined at the top to
## fit this curve
def fano(x, x0, b, c, A, e):
    """The Fano lineshape for reflection.

    x: x coordinates
    x0: Peak position
    b: Peak width
    c: Asymmetry parameter
    A: Amplitude
    e: Offset

    y: The y coordinates of the Fano lineshape"""
    eps1 = 2*(x-x0)/b1
    f1 = (eps+c)**2/(eps**2+1)
    y = A*f+e
    return y

def f_lsq(params, x, y_meas):
    """ Computes the deviation of spetrum data
    from a Fano lineshape.

    params: List of Fano parameters x0, b, c, A, e
    x: the x coordinates of the measurement
    y: the measured y data

    res: the residules
    """
    y_fan = fano(x, *params)
    res = y_fan-y_meas
    return res

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
