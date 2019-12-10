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
    eps = 2*(x-x0)/b
    f = (eps+c)**2/(eps**2+1)
    y = A*f+e
    return y

def fano_residuals(params, x, y_meas):
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
