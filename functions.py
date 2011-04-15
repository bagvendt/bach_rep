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
import scipy.signal as sig
from constants import *
import copy
import time

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
	env['org_img'] = copy.deepcopy(img)
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
#	img = pylab.flipud(img)
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
			G = frac*math.exp(enum/float(denom))
			img[i1][i2] = img[i1][i2] * G
	return (img,env)

def gaussian_blur_conv(img,env,**kwargs):
## Math from : http://en.wikipedia.org/wiki/Gaussian_blur
	sigma = kwargs['sigma']
	x_0, y_0 = img.shape
	edgemap = numpy.arange(25,dtype='f').reshape(5,5)*0
	print img.shape,edgemap.shape
	for i1 in range(-2,3):
		for i2 in range(-2,3):
			ii1 = i1 + 2
			ii2 = i2 + 2
			enum_x = (i1) ** 2  
			enum_y = (i2) ** 2  
			enum = -enum_x-enum_y
			denom = 2 * (sigma ** 2)
			frac = (1/(2*math.pi*(sigma**2)))
			edgemap[ii1][ii2] = frac*math.exp(enum/float(denom))
	#edgemap,env = invert_dimensions(edgemap,env,**kwargs)
	out = sig.fftconvolve(img,edgemap,"same")
	print out.shape
	return (out,env)

def gaussian_blur_matrix_conv(img,env,**kwargs):
	return (sig.fftconvolve(img,GAUSS,"same"),env)

def rigmor_sobel(img,env,**kwargs):
	"""TODO: Maybe og fucking garanteret different name"""
	maxval = 0
	vert = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	hor  = numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]])
	dim_x,dim_y = vert.shape
	G_x = sig.fftconvolve(img,vert)
	G_y = sig.fftconvolve(img,hor)
	G = numpy.sqrt(G_x**2 + G_y ** 2)
	for i1,a in enumerate(G):
		for i2,b in enumerate(a):
			if G[i1][i2] > maxval:
				maxval = G[i1][i2]
	env['sobel'] = G
	env['G_x'] = G_x
	env['G_y'] = G_y
	env['maxval'] = maxval
	print G[55][50]
	return (G,env)

def low_pass(img,env,**kwargs):
	n,m = img.shape
	x,y = n/2,m/2
	cutoff = 200
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			if numpy.sqrt(((i1-x) ** 2) + ((i2-y)**2)) > cutoff: 
				img[i1][i2] = 0
	return (img,env)

def gaussderiv(img,env,**kwargs):
	img = sig.fftconvolve(img,MEXHAT_LARGE,"same")	
	return (img,env)

def edge_improved(img,env,**kwargs):
	orig_img = img
	deriv = sig.fftconvolve(orig_img, MEXHAT_SMALL,"same")
	sobel = env['sobel']
	w,h = orig_img.shape
	for i,a in enumerate(deriv):
		for j,b in enumerate(a):
			if ((i < w -2 ) and (j < h-2)):
				if (abs(b)+deriv[i+1][j]+deriv[i][j+1] == abs(b)+abs(deriv[i+1][j]) + abs(deriv[i][j+1])):
					sobel[i][j] = 0
			else:
				sobel[i][j] = 0
	env['improved_edgemap'] = sobel
	return (sobel,env)

def threshold_and_edgemap(img,env,**kwargs):
	threshold = kwargs['threshold']
	maxval = env['maxval']
	G_x = env['G_x']
	G_y = env['G_y']
	w,h = img.shape
	edgemap = numpy.arange(w*h).reshape(w,h)*0
	dirmap = numpy.arange(w*h).reshape(w,h)*0
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			if img[i1][i2]/maxval*255 >= threshold:
				edgemap[i1][i2] = 255
				dirmap[i1][i2] = math.atan2(-G_y[i1][i2],G_x[i1][i2]) #Har aendret til -y,x for at faa vinkelret linje.
				if dirmap[i1][i2] > PI_2:
					dirmap[i1][i2] -= PI_2
				if dirmap[i1][i2] < -PI_2:
					dirmap[i1][i2] += PI_2
	env['edgemap'] = edgemap
	env['dirmap'] = dirmap
	return (dirmap,env)

def sign(a):
	if a > 0:
		return 1
	else:
		return -1

def abspace(img,env,**kwargs):
	minr = kwargs['minr']
	maxr = kwargs['maxr']
	edgemap = env['edgemap']
	dirmap = env['dirmap']
	w,h = img.shape
	abspace = numpy.arange(w*h).reshape(w,h)*0

	for i1,a in enumerate(edgemap):
		print str(i1*100/w)+"%"
		for i2,b in enumerate(a):
			if edgemap[i1][i2] == 0: 
				continue
			x = minr*math.cos(dirmap[i1][i2])
			y = minr*math.sin(dirmap[i1][i2])
			if (dirmap[i1][i2] > -PI_4) and (dirmap[i1][i2] < PI_4):
				dx = sign(x)
				dy = dx*math.tan(dirmap[i1][i2])
			else:
				dy = sign(y)
				dx = dy/math.tan(dirmap[i1][i2])
			#abspace[y1][x1]
			while math.sqrt(x**2+y**2) < maxr:
				x1 = i2+x 
				y1 = i1-y
				x2 = i2-x
				y2 = i1+y
				if((x1<w) and (x1>=0) and (y1<h) and (y1>=0)):
					abspace[x1][y1] += edgemap[i1][i2] / math.sqrt(x**2+y**2)
				if((x2<w) and (x2>=0) and (y2<h) and (y2>=0)):
					abspace[x2][y2] += edgemap[i1][i2] / math.sqrt(x**2+y**2)
				x = x+dx
				y = y+dy
	env['abspace'] = abspace
	return (abspace,env)

def abspace_threshold(img,env,**kwargs):
	orig = env['org_img']
	centers = []
	for i1,a in enumerate(img):
		for i2,a in enumerate(a):
			if img[i1][i2] > 25:
				img[i1][i2] = 255
				orig[i1][i2] = 0
				centers.append((i1,i2))
			else:
				img[i1][i2] = 0
	radi = 100
	
	for i1,a in enumerate(orig):
		for i2,b in enumerate(a):
			for center in centers:
				if numpy.sqrt((i1-center[0])**2+(i2-center[1])**2) in range(radi-3,radi+3):
					orig[i1][i2] = 0
	return (orig,env)

def gaussian_derived(img,env,**kwargs):
	start = time.time()
## Math from : http://en.wikipedia.org/wiki/Gaussian_filter
	sigma = kwargs['sigma']
	Gx = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	Gy = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0

	max_i = 0
	for i1,a in enumerate(img):
		for i2,b in enumerate(a):
			Gx[i1][i2] = (-1*i1*math.exp((-(i2**2)-(i1**2))/float(2*sigma**2)))/float(2*PI*sigma**4)*img[i1][i2]
			Gy[i1][i2] = (-1*i2*math.exp((-(i2**2)-(i1**2))/float(2*sigma**2)))/float(2*PI*sigma**4)*img[i1][i2]
	
	Gi = numpy.sqrt(Gx**2+Gy**2)

	return (Gi,env)

def gaussian_derived_conv(img,env,**kwargs):
	start = time.time()
## Math from : http://en.wikipedia.org/wiki/Gaussian_filter
	sigma = kwargs['sigma']
	Gx = numpy.arange(25,dtype='f').reshape(5,5)*0
	Gy = numpy.arange(25,dtype='f').reshape(5,5)*0

	for i1 in range(-2,3):
		for i2 in range(-2,3):
			ii1 = i1+2
			ii2 = i2+2
			Gx[ii1][ii2] = (-1*i2*math.exp((-(i2**2)-(i1**2))/float(2*sigma**2)))/float(2*PI*sigma**4)
			Gy[ii1][ii2] = (-1*i1*math.exp((-(i2**2)-(i1**2))/float(2*sigma**2)))/float(2*PI*sigma**4)
	print Gx
	print Gy
	Gi_x = sig.fftconvolve(img,Gx,"same")
	Gi_y = sig.fftconvolve(img,Gy,"same")
	Gi = numpy.sqrt(Gi_x**2+Gi_y**2)
	return (Gi,env)

def hat_convolve(img,env,**kwargs):
	#outimg = sig.fftconvolve(img,PIXEL_HAT,"full")
	outimg = sig.fftconvolve(img,CELL_HAT2,"full")
	return (outimg,env)


def convolve_test(img,env,**kwargs):
	a = numpy.arange(10).reshape(2,5)
	img = scipy.signal.fftconvolve(img,a)
	return (img,env)

def invert_dimensions(img,env,**kwargs):
	w,h = img.shape
	newimg = numpy.arange(w*h,dtype='f').reshape(w,h)*0
	w1=0
	while w1 < w:
		h1 = 0
		while h1 < h:
			newimg[w1][h1] = img[w-w1-1][h-h1-1]
			h1 = h1+1
		w1= w1+1
	return (newimg,env)

def invert_color(img,env,**kwargs):
	return (img*(-1),env)
	for x,a in enumerate(img):
		for y,b in enumerate(a):
			img[x][y] = numpy.abs(img[x][y]-255)
	return (img,env)

def image_convolve_threshold(img,env,**kwargs):
	w,h = img.shape
	thres = kwargs['threshold']
	newimg = numpy.arange(w*h,dtype='f').reshape(w,h)*0
	print "Doing threshold"
	for x,a in enumerate(img):
		for y,b in enumerate(a):
			if img[x][y] >= thres:
				newimg[x][y] = 255
			else:
				newimg[x][y] = 0
	env['img_conv_thres'] = newimg
	return (newimg,env)
			
def image_convolve_draw_circles(img,env,**kwargs):
	print "Drawing circles"
	circle_radius = kwargs['circle_radius']
	org_img = env['org_img']
	thres_img = env['img_conv_thres']
	for x, a in enumerate(thres_img):
		for y,b in enumerate(a):
			if thres_img[x][y] == 255:
				angle = 0
				while angle<360:
					x1 = int((circle_radius)*numpy.cos(angle))
					y1 = int(circle_radius*numpy.sin(angle))
					if x+x1 in range(0,org_img.shape[0]) and y+y1 in range(0,org_img.shape[1]):
						org_img[x+x1][y+y1] = 123
					angle += 1
	return (org_img,env)

def image_convolve(img,env,**kwargs):
	image = kwargs['image']

	testimage = pylab.imread(image)	
	testimage = toimage(testimage)
	testimage = testimage.convert("L")
	testimage = fromimage(testimage)

	testimage,PLACEHOLDER = invert_color(testimage,env,**kwargs)
	testimage,PLACEHOLDER = invert_dimensions(testimage,env,**kwargs)		
	testimage_sum = sum(sum(testimage**2))
	outimg = sig.fftconvolve(img,testimage/float(testimage_sum),"same")
	return (outimg,env)

def image_convolve_v2(img,env,**kwargs):
	image = kwargs['image']

	testimage = pylab.imread(image)	
	testimage = toimage(testimage)
	testimage = testimage.convert("L")
	testimage = fromimage(testimage)

	testimage,PLACEHOLDER = invert_color(testimage,env,**kwargs)
	testimage,PLACEHOLDER = invert_dimensions(testimage,env,**kwargs)		
	testimage_sum = sum(sum(testimage**2))
	
	img1 = sig.fftconvolve(testimage,testimage/float(testimage_sum),"same")
	img2 = sig.fftconvolve(img,img/float(testimage_sum),"same")
	img3 = sig.fftconvolve(img,testimage/float(testimage_sum),"same")
	print img1.shape,img2.shape,img3.shape
	outimg = img1+img2-img3
	return (outimg,env)

def difference_of_gaussians(img,env,**kwargs):
	K = kwargs['K']**2
	sigma = kwargs['sigma']
	#Gauss = numpy.arange(25,dtype='f').reshape(5,5)*0
	#for i1 in range(-2,3):
	#	for i2 in range(-2,3):
	#		ii1 = i1 + 2
	#		ii2 = i2 + 2
	Gauss = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	for i1 in range(-img.shape[0]/2,img.shape[0]/2+1):
		for i2 in range(-img.shape[1]/2,img.shape[1]/2+1):
			ii1 = i1 + img.shape[0]/2
			ii2 = i2 + img.shape[1]/2
			enum_x = (i1) ** 2  
			enum_y = (i2) ** 2  
			enum = -enum_x-enum_y
			denom1 = 2 * (sigma ** 2)
			frac1 = (1/(2*math.pi*(sigma**2)))
			

			denom2 = 2*K*(sigma**2)
			frac2 = (1/(2*K*math.pi*(sigma**2)))
			G1 = frac1*math.exp(enum/float(denom1))
			G2 = frac2*math.exp(enum/float(denom2))
			Gauss[ii1][ii2] = G1 - G2
	
	
	img1 = sig.fftconvolve(img,Gauss,"same")

	return (img1,env)

def sum_of_gaussians(img,env,**kwargs):
	K = kwargs['K']**2
	sigma = kwargs['sigma']
	#Gauss = numpy.arange(25,dtype='f').reshape(5,5)*0
	#for i1 in range(-2,3):
	#	for i2 in range(-2,3):
	#		ii1 = i1 + 2
	#		ii2 = i2 + 2
	Gauss = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	for i1 in range(-img.shape[0]/2,img.shape[0]/2+1):
		for i2 in range(-img.shape[1]/2,img.shape[1]/2+1):
			ii1 = i1 + img.shape[0]/2
			ii2 = i2 + img.shape[1]/2
			enum_x = (i1) ** 2  
			enum_y = (i2) ** 2  
			enum = -enum_x-enum_y
			denom1 = 2 * (sigma ** 2)
			frac1 = (1/(2*math.pi*(sigma**2)))
			

			denom2 = 2*K*(sigma**2)
			frac2 = (1/(2*K*math.pi*(sigma**2)))
			G1 = frac1*math.exp(enum/float(denom1))
			G2 = frac2*math.exp(enum/float(denom2))
			Gauss[ii1][ii2] = G1 + G2
	
	
	img1 = sig.fftconvolve(img,Gauss,"same")

	return (img1,env)

def difference_of_derived_gaussians(img,env,**kwargs):
	sigma1 = kwargs['sigma1']
	sigma2 = kwargs['sigma2']
	#Gx = numpy.arange(25,dtype='f').reshape(5,5)*0
	#Gy = numpy.arange(25,dtype='f').reshape(5,5)*0
	#for i1 in range(-2,3):
	#	for i2 in range(-2,3):
	#		ii1 = i1 + 2
	#		ii2 = i2 + 2
	Gx = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	Gy = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	for i1 in range(-img.shape[0]/2,img.shape[0]/2+1):
		for i2 in range(-img.shape[1]/2,img.shape[1]/2+1):
			ii1 = i1 + img.shape[0]/2
			ii2 = i2 + img.shape[1]/2
			Gx[ii1][ii2] = (-1*i2*math.exp((-(i2**2)-(i1**2))/float(2*sigma1**2)))/float(2*PI*sigma1**4)
			Gy[ii1][ii2] = (-1*i1*math.exp((-(i2**2)-(i1**2))/float(2*sigma2**2)))/float(2*PI*sigma2**4)
	
	Gi_x = sig.fftconvolve(img,Gx,"same")
	Gi_y = sig.fftconvolve(img,Gy,"same")
	Gi = numpy.sqrt(Gi_x**2-Gi_y**2)

	return (Gi,env)

def sum_of_derived_gaussians(img,env,**kwargs):
	sigma1 = kwargs['sigma1']
	sigma2 = kwargs['sigma2']
	#Gx = numpy.arange(25,dtype='f').reshape(5,5)*0
	#Gy = numpy.arange(25,dtype='f').reshape(5,5)*0
	#for i1 in range(-2,3):
	#	for i2 in range(-2,3):
	#		ii1 = i1 + 2
	#		ii2 = i2 + 2
	Gx = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	Gy = numpy.arange(img.shape[0]*img.shape[1],dtype='f').reshape(img.shape[0],img.shape[1])*0
	for i1 in range(-img.shape[0]/2,img.shape[0]/2+1):
		for i2 in range(-img.shape[1]/2,img.shape[1]/2+1):
			ii1 = i1 + img.shape[0]/2
			ii2 = i2 + img.shape[1]/2
			Gx[ii1][ii2] = (-1*i2*math.exp((-(i2**2)-(i1**2))/float(2*sigma1**2)))/float(2*PI*sigma1**4)
			Gy[ii1][ii2] = (-1*i1*math.exp((-(i2**2)-(i1**2))/float(2*sigma2**2)))/float(2*PI*sigma2**4)
	
	Gi_x = sig.fftconvolve(img,Gx,"same")
	Gi_y = sig.fftconvolve(img,Gy,"same")
	Gi = numpy.sqrt(Gi_x**2+Gi_y**2)

	return (Gi,env)

def convolve_test(img,env, **kwargs):
	image = kwargs['template']
	template = pylab.imread(image)	
	template = toimage(template)
	template = template.convert("L")
	template = fromimage(template)
	
	#img = numpy.arange(10*10).reshape(10,10)*0
	#img[2][2] = img[2][3] = img[1][3] = 1
	temp = numpy.arange(4).reshape(2,2)*0
	temp[1][0] = temp[1][1] = temp[0][1] = 1
	temp,env = invert_dimensions(temp,env)
	#template = temp

	w,h = img.shape
	tw,th = template.shape
	canvas = numpy.arange(w*h,dtype='f').reshape(w,h)*00
	temp_sum = sum(sum(template))
	for wi in range(w):
		for hi in range(h):
			if (wi+tw-1 >= w or hi+th-1 >= h):
				continue
			#if (hi is not 0):
			#	continue
			#print wi,hi
			cut = img[wi:wi+tw]
			#print cut
			cut = map(lambda x: x[hi:hi+th] ,cut)
			#print cut
			val = numpy.sqrt((sum(sum(cut)) - temp_sum) **2)
			#canvas[hi+(th/2)][wi+(tw/2)] = val
			canvas[wi+(tw/2)][hi+(th/2)] = val
			#canvas[wi+(tw/2)][hi+(th/2)] = 1
	print canvas
	return (canvas,env)

def image_convolve_scen1(img,env,**kwargs):
	image = kwargs['template']
	template = pylab.imread(image)	
	template = toimage(template)
	template = template.convert("L")
	template = fromimage(template )
	w,h = img.shape
	tw,th = template.shape
	canvas = numpy.arange(w*h,dtype='f').reshape(w,h)*00
	template_trans = numpy.transpose(template)
	template_ost = numpy.dot(template_trans, template)
	for wi in range(w):
		for hi in range(h):
			if (wi+tw-1 >= w or hi+th-1 >= h):
				continue
			cut = img[wi:wi+tw]
			cut = map(lambda x: x[hi:hi+th] ,cut)
			val = numpy.dot(numpy.transpose(cut),cut) + template_ost - 2*numpy.dot(numpy.transpose(cut), template)
			canvas[wi+(tw/2)][hi+(th/2)] = sum(sum(val))
	print canvas
	return (canvas,env)

	template,PLACEHOLDER = invert_color(template,env,**kwargs)
	template,PLACEHOLDER = invert_dimensions(template,env,**kwargs)		
