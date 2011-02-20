from scipy import *
#Andre ting jeg har laert. Imread1 er den der fatter at flatten skal grayscale
from scipy.misc import imread as imread1
import numpy as npy
from pylab import *
from scipy.ndimage import gaussian_filter

def test():
	#flatten=1 gor ting grayscaled.
	img = imread1('../Billeder/celle1.png',flatten=1).astype('float32')
	img = fft2(img)
	img = gaussian_filter(abs(img),0.0044)
	#img = ifft2(img)
	img = fftshift(img)
	print img
	imshow(img)
	show()
	

test()
