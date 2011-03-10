from functions import *
from leg import *

smooth_test = ( 
	'../img/test20_57.jpg',
	[(fft2,{}),
	(fftshift,{}),
	(gaussian_blur,{'sigma':15,
			}),
	(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)

sobel_test = ( 
	'img/engine.PNG',
	[
	#(fft2,{}),
	#(fftshift,{}),	
	(rigmor_sobel,{}),
	#(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)

epic_test = ( 
	'../img/test20_57.jpg',
	[
	#(fft2,{}),
	#(fftshift,{}),
	#(gaussian_blur,{'sigma':15,}),
	#(ifft2,{}),
	(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':40}),
	(edge_improved,{}),
	#(abspace,{
	#	'minr':5,
	#	'maxr':10,
	#}),
	(abs_func,{}),
	(display,{})],
	)

displayy = ( 
	'img/test.jpg',
	[
	(display,{})],
	)

mexican_test = ( 
	'../img/test20_57.jpg',
	[(gaussderiv,{}),
	(display,{})],
	)

sobel_together_with_a_mexican = ( 
	'../img/test20_57.jpg',
	[(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':40}),
	(edge_improved,{}),
	(display,{})],
	)

edgemap_test = ( 
	'../img/test20_57.jpg',
	[
	(rigmor_sobel,{}),
	(threshold_and_edgemap,{'threshold':80}),
	(edge_improved,{}),
	(abspace,{
		'minr':1,
		'maxr':2,
	}),
	(display,{})],
	)

#Remember to add new procedures to this list
func_list = [smooth_test,sobel_test,epic_test,mexican_test,sobel_together_with_a_mexican,edgemap_test]
