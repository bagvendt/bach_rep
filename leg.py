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

def penis(img,env,**kwargs):
	w,h = img.shape 
	lut = numpy.arange(w*h).reshape(w,h) * 0
	for i in range(0,240):
		lut[i,i] = 255
	return (lut,env)

def hough_run(img,env,**kwargs):
	#offx = r.x;
	#offy = r.y;
	#width = r.width;
	#height = r.height;
	#offset = ip.getWidth()
	radiusMin = 10
	radiusMax = 20 
	radiusInc = 2
	w,h = img.shape
	depth = int(round(((radiusMax-radiusMin)/float(radiusInc)))+1)
	lutsize, lut = buildlookuptable(radiusMin,radiusMax,radiusInc,depth)

	houghmap = houghTransform(lut,lutsize,radiusMin,radiusMax,radiusInc,w,h,depth,img)
	img = createHoughPixels(houghmap,w,h)
	#print img
	img = draw_center_points(img,900,houghmap,radiusMin,radiusMax,radiusInc,h,w)
	return (img,env)


def buildlookuptable(radiusMin,radiusMax,radiusInc,depth):
	incDen = int(round(float(8) * radiusMin))
	print incDen,'incden',depth,'depth'
	lut = numpy.arange(depth*incDen*2).reshape(2,incDen,depth) * 0
	for radius in range(radiusMin,radiusMax+1,radiusInc):
		i = 0
		print radius
		for incNun in range(incDen):
			angle = (2*math.pi * float(incNun)) / float(incDen)
			indexR = int((radius-radiusMin)/float(radiusInc))
			#print indexR,'indexR'	
			#print indexR
			rcos = int(round(float(radius) * math.cos(angle)))
			#print rcos,'rcos'
			rsin = int(round(float(radius) * math.sin(angle)))
			print rsin,'rsin'
			if((i == 0) or (rcos != lut[0,i,indexR]) and (rsin != lut[1,i,indexR])):
				lut[0,i,indexR] = rcos
				lut[1,i,indexR] = rsin
				i += 1
	print i,'lutSize'
	return (i,lut)



def houghTransform(lut,lutsize,radiusMin,radiusMax,radiusInc,width,height,depth,img):
	houghValues = numpy.arange(width*height*depth).reshape(width,height,depth) * 0
	k = width - 1
	l = height - 1
	for x in range(width):
		for y in range(height):
			for radius in range(radiusMin,radiusMax+1,radiusInc):
				if(img[x][y] != 0):
					indexR = (radius-radiusMin) / radiusInc
					print ((x+1)*100) / (width)
					for i in range(lutsize):
						a = x + lut[1,i,indexR]
						b = y + lut[0,i,indexR]
						#print a,b,x,y,indexR
						if ((b >= 0) and (b < height) and (a >= 0) and (a < width)):
							houghValues[a,b,indexR] += 1;
	return houghValues


def createHoughPixels(houghValues,width,height):
	d = -1.0
	"""
	kan muligvis udskiftes med
	d = max(houghValues)
	"""
	#print houghValues
	for x in range(width):
		for y in range(height):
			if (houghValues[x,y,0] > d):
				d = houghValues[x,y,0]
	houghPixels = numpy.arange(width*height*1).reshape(width,height) * 0
	for x in range(width):
		for y in range(height):
			#print houghValues[x,y,0]
			#print d 
			houghPixels[x,y] = round((houghValues[x,y,0] * 255.0) / d)

	return houghPixels


def draw_center_points(img,maxCircles,houghValues,radiusMin,radiusMax,radiusInc,height,width):
	xMax = 0
	yMax = 0
	rMax = 0
	canvas = numpy.arange(width*height*1).reshape(width,height) * 0
	for i in range(0,maxCircles):
		counterMax = -1
		for radius in range(radiusMin,radiusMax+1,radiusInc):
			indexR = (radius-radiusMin)/radiusInc
			for y in range(height):
					for x in range(width):
						if(houghValues[x,y,indexR] > counterMax):
							print 'NU'
							counterMax = houghValues[x,y,indexR]
							xMax = x
							yMax = y
							rMax = radius
							print x,y
							canvas[x,y] = 239 
							canvas[x,y+1] = 239
							canvas[x+1,y+1] = 239
							canvas[x+1,y] = 239
							canvas[x-1,y] = 239
	return canvas
