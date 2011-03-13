import scipy
from scipy.misc import imread as imread1
from scipy.misc import toimage,fromimage
import numpy
from pylab import imread, gray
import pylab
import scipy.signal
from scipy.ndimage import gaussian_filter
from proc import *
import matplotlib.pyplot as plt
import Image,ImageFilter,ImageOps
import math
import scipy.signal as sig

def manual_gauss(img,env,**kwargs):
	sigma = kwargs['sigma']
	x0 = kwargs['x0']
	y0 = kwargs['y0']
	w,h = img.shape
	deriv = numpy.arange(w*h).reshape(w,h)*0
	dev_x = numpy.arange(w*h).reshape(w,h)*0
	dev_y = numpy.arange(w*h).reshape(w,h)*0
	A = (-math.sqrt(2)/(4*math.sqrt(math.pi*(sigma**2))*(sigma**2)))
	for x,a in enumerate(img):
		print str(x*100/w)+"%"
		for y,b in enumerate(a):
			dev_x[x][y] = A*(2*x-2*x0)*numpy.exp((-(x-x0)**2-(y-y0)**2)/2*(sigma**2))
			dev_y[x][y] = A*(2*y-2*y0)*numpy.exp((-(x-x0)**2-(y-y0)**2)/2*(sigma**2))
	new_x = sig.convolve2d(img, dev_x)
	new_y = sig.convolve2d(img, dev_y)
	deriv = numpy.sqrt(new_x**2+new_y**2)
	
	return (deriv,env)
