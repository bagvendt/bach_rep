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

def smooth(img,env,**kwargs):
	"""TODO: Maybe different name"""
	dim = img.size
	h,w = img.shape
	new = numpy.arange(dim).reshape(h,w) * 0
	h1,w1 = new.shape


	sigma_x = kwargs['sigma_x']
	sigma_y = kwargs['sigma_y']
	x_0 = kwargs['x_0']
	y_0 = kwargs['x_0']
	A = kwargs['A']
	"""
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			enum_x = (i1 - x_0) ** 2  
			enum_y = (i2 - y_0) ** 2  
			denom_x = 2 * (sigma_x **2)  
			denom_y = 2 * (sigma_y **2)  
			var_var = A * math.exp(-(enum_x/float(denom_x)) + (enum_y/float(denom_y)))
			print var_var
			new[i1][i2] = var_var
	img = new * img 
	"""
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			img[i1][i2] = img[i1][i2] * gaussian_copy(A,x_0,y_0,sigma_x,sigma_y)(i1,i2)
	return (img,env)
	
# Nedenstaaende er fra http://www.scipy.org/Cookbook/FittingData#head-11870c917b101bb0d4b34900a0da1b7deb613bf7
def gaussian_copy(height, center_x, center_y, width_x, width_y):
	"""Returns a gaussian function with the given parameters"""
	width_x = float(width_x)
	width_y = float(width_y)
	return lambda x,y: height*math.exp(-(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)	

