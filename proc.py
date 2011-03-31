from functions import *
from leg import *

smooth_test = ( 
	'img/cykel.jpg',
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
	'img/cirkel.png',
	[
	(fft2,{}),
	(fftshift,{}),
	(gaussian_blur,{'sigma':15,}),
	(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)
ghost1 = ('img/cirkel.png',
	[	
	(gaussian_blur_conv,{'sigma':15,}),
	(abs_func,{}),
	(display,{})],
	)

ghost2 = ('img/circ2.png', #circ2
	[
	(invert_color,{}),
	(image_convolve,{'image':"img/circ.png"}), # circ
	(image_convolve_threshold,{'threshold':0.95,}), # circ = circ3 = 0.95
	(image_convolve_draw_circles,{'circle_radius':58,}), # 58 = circ, 12 = circ3
	#(invert_dimensions,{}),	
	(display,{})],
	)

#Remember to add new procedures to this list
func_list = [ghost,ghost1,ghost2, smooth_test,sobel_test,epic_test,mexican_test,sobel_together_with_a_mexican,edgemap_test,edgemap_test2,manual_gauss_test]
