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
	edgemap = numpy.arange(w*h).reshape(w,h)*0
	for x,a in enumerate(G):
		for y,b in enumerate(a):
			dev_x = (-1/(4*math.sqrt(math.pi*(sigma**2))*(sigma**2))*math.sqrt(2)*(2*x-2*x0)*math.exp((-(x-x0)**2-(y-y0)**2)/2*(sigma**2))
			dev_y = (-1/(4*math.sqrt(math.pi*(sigma**2))*(sigma**2))*math.sqrt(2)*(2*y-2*y0)*math.exp((-(x-x0)**2-(y-y0)**2)/2*(sigma**2))
			dev[x][y] = math.sqrt(dev_x**2+dev_y**2)
	
