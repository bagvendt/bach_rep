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

def gaussian_blur(img,env,**kwargs):
## Math from : http://en.wikipedia.org/wiki/Gaussian_blur
	sigma = kwargs['sigma']
	x_0, y_0 = img.shape
	x_0 = x_0 / 2
	y_0 = y_0 / 2
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			enum_x = (i1 - x_0) ** 2  
			enum_y = (i2 - y_0) ** 2  
			enum = -enum_x-enum_y
			denom = 2 * (sigma ** 2)
			frac = (1/(2*math.pi*(sigma**2)))
			G = frac*math.exp(enum/denom)
			img[i1][i2] = img[i1][i2] * G
	return (img,env)

def rigmor_sobel(img,env,**kwargs):
	"""TODO: Maybe og fucking garanteret different name"""
	vert = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	hor  = numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]])
	#G_x = numpy.fft.fft2(img) * numpy.fft.fft2(vert)
	#G_y = numpy.fft.fft2(img) * numpy.fft.fft2(hor)
	G_x = scipy.signal.sepfir2d(img, [1,2,1], [1,0,-1])
	G_y = scipy.signal.sepfir2d(img, [1,0,-1], [1,2,1])
	G = numpy.sqrt(G_x**2 + G_y ** 2)	
	return (G,env)