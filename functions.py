import scipy
#Andre ting jeg har laert. Imread1 er den der fatter at flatten skal grayscale
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

"""
When implementing new functions functions should be of the form
fname(img,env, **kwargs)
and fname should return the tuple (img,env)
"""

def setup(image,env):
	"""Loads the image and sets up the environment"""
	#flatten=1 makes image grayscaled.
	#img = imread1(image,flatten=1).astype('float32')	
	img = pylab.imread(image)	
	img = toimage(img)
	#r,g,b = img.split()
	#img = img.draft('L',img.size)
	#img = ImageOps.grayscale(img)
	img = img.convert("L")
	img = fromimage(img)	
	#img = Image.merge("RGB", (g,g,g))
	return (img,env)

def display(img,env,**kwargs):
	"""Displays the image
	This function has some limitations as it is only possible to
	show one image per time the script is run.
	Futhermore the script returns the tuple (img,env) which doesn't make
	any sense atm.
	"""
	pylab.figure()
	img = pylab.flipud(img)
	pylab.imshow(img)
	pylab.gray()
	pylab.show()

	return (img,env)

def abs_func(img,env,**kwargs):
	#Remember that abs is correcly manipulating the values piecewise
	img = numpy.abs(img)
	return (img,env)

def fft2(img,env,**kwargs):
	img = numpy.fft.fft2(img)
	return (img,env)

def ifft2(img,env,**kwargs):
	img = numpy.fft.ifft2(img)
	return (img,env)

def rfft2(img,env,**kwargs):
	img = numpy.fft.rfft2(img)
	return (img,env)

def irfft2(img,env,**kwargs):
	img = numpy.fft.irfft2(img)
	return (img,env)

def gauss(img,env,**kwargs):
	value = kwargs['value']
	img = gaussian_filter(img,value, )
	return (img,env)


def fftshift(img,env,**kwargs):
	img = numpy.fft.fftshift(img)
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

def low_pass(img,env,**kwargs):
	"""
	Needs more work. 
	Needs to be dynamic. Non static cutoff and size values
	"""
	print img.dtype
	n,m = 360,480
	x,y = n/2,m/2
	cutoff = 200
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			if numpy.sqrt(((i1-x) ** 2) + ((i2-y)**2)) > cutoff: 
				img[i1][i2] = 0
			
			#for i3,c in enumerate(b):
			#	if numpy.sqrt(((u-x) ** 2) + ((v-y)**2)) > cutoff: 
			#		img[i1][i2] var = numpy.sqrt(i)
			#	var = numpy.sqrt(i)
	


	return (img,env)


def convolve_test(img,env,**kwargs):
	a = numpy.arange(10).reshape(2,5)
	img = scipy.signal.fftconvolve(img,a)
	return (img,env)

