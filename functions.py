import scipy
#Andre ting jeg har laert. Imread1 er den der fatter at flatten skal grayscale
from scipy.misc import imread as imread1
import numpy
import pylab
from scipy.ndimage import gaussian_filter
from proc import *

def setup(image,env):
	"""Loads the image and sets up the environment"""
	#flatten=1 makes image grayscaled.
	img = imread1(image,flatten=1).astype('float32')
	return (img,env)

def display(img,env,**kwargs):
	pylab.figure()
	pylab.imshow(img)
	pylab.show()
	return (img,env)

def abss(img,env,**kwargs):
	img = abs(img)
	return (img,env)

def fft2(img,env,**kwargs):
	img = numpy.fft.fft2(img)
	return (img,env)

def gauss(img,env,**kwargs):
	#Remember that abs is correcly manipulating the values piecewise
	value = kwargs['value']
	img = gaussian_filter(abs(img),value)
	return (img,env)

def ifft2(img,env,**kwargs):
	img = numpy.fft.ifft2(img)
	return (img,env)

def fftshift(img,env,**kwargs):
	img = numpy.fft.fftshift(img)
	return (img,env)

