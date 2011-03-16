from functions import *
from leg import *

smooth_test = ( 
	'img/dots.png',
	[(fft2,{}),
	(fftshift,{}),
	(gaussian_blur,{'sigma':15,
			}),
	(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)

sobel_test = ( 
	'img/dots.png',
	[
	(fft2,{}),
	#(fftshift,{}),	
	(gaussian_blur,{'sigma':15,}),
	(ifft2,{}),
	(rigmor_sobel,{}),
	(abs_func,{}),
	(display,{})],
	)

epic_test = ( 
	'img/dots.png',
	[
	#(fft2,{}),
	#(fftshift,{}),
	#(gaussian_blur,{'sigma':15,}),
	#(ifft2,{}),
	(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':40}),
	#(edge_improved,{}),
	(abspace,{
		'minr':5,
		'maxr':10,
	}),
	(abs_func,{}),
	(display,{})],
	)

displayy = ( 
	'img/dots.png',
	[
	(display,{})],
	)

mexican_test = ( 
	'img/dots.png',
	[(gaussderiv,{}),
	(display,{})],
	)

sobel_together_with_a_mexican = ( 
	'img/dots.png',
	[(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':40}),
	(edge_improved,{}),
	(display,{})],
	)

edgemap_test = ( 
	'img/dots.png',
	[
	(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':80}),
	#(edge_improved,{}),
	(abspace,{
		'minr':50,
		'maxr':200,
	}),
	(display,{})],
	)

edgemap_test2 = ( 
	'img/dots.png',
	[
	(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':80}),
	#(edge_improved,{}),
	(abspace,{
		'minr':80,
		'maxr':130,
	}),
	(abspace_threshold,{}),
	(display,{})],
	)

manual_gauss_test = ( 
	'img/cirkel.png',
	[
	(manual_gauss,{
		'sigma':200,
		'x0':100,
		'y0':100
	}),
	(display,{})],
	)
ghost = ( 
	'../img/celle1.png',
	[
	#(fft2,{}),
	#(fftshift,{}),
	(gaussian_derived_conv,{'sigma':3,}),
	#(ifft2,{}),
	#(abs_func,{}),
	#(rigmor_sobel,{}),
	#(hough_run,{}),
	(display,{})],
	)
ghost1 = ( 
	'../img/celle1.png',
	[
	#(fft2,{}),
	#(gaussian_blur,{'sigma':2,}),
	(gaussian_blur_conv,{'sigma':2,}),
	#(ifft2,{}),
	#(abs_func,{}),
	(display,{})],
	)

ghost2 = ('../img/celle1.png',
	[
	#(image_convolve,{'images':["img/single_cell_1.png"]}),
	(hat_convolve,{}),
	(display,{})],
	)

#Remember to add new procedures to this list
func_list = [ghost,ghost1,ghost2, smooth_test,sobel_test,epic_test,mexican_test,sobel_together_with_a_mexican,edgemap_test,edgemap_test2,manual_gauss_test]
