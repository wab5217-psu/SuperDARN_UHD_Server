import numpy as np
import scipy.signal as sig
import scipy.ndimage
import pdb

# samples - input samples of rate rate
# trise - freq in kHz
# rate - sampling rate, in Hz
def gaussian_pulse(samples, trise, rate):
    # generate filter coefficients
    gauss_sigma = rate / (trise * 1000.0)
    
    filt_real = scipy.ndimage.filters.gaussian_filter1d(np.real(samples), gauss_sigma)
    filt_imag = scipy.ndimage.filters.gaussian_filter1d(np.imag(samples), gauss_sigma)
    
    pdb.set_trace()
    return filt_real + 1j * filt_imag
