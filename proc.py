from functions import *
from leg import *

smooth_test = ( 
	'../img/celle1.png',
	[(fft2,{}),
	(smooth,{'sigma_x':140,
			 'sigma_y':140,
			 'x_0':180,
			 'y_0':240,
			 'A':1,
			}),
	(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)

sobel_test = ( 
	'../img/celle1.png',
	[(rigmor_sobel,{}),
	(display,{})],
	)

epic_test = ( 
	'../img/cykel.jpg',
	[(fft2,{}),
	(smooth,{'sigma_x':120,
			 'sigma_y':120,
			 'x_0':180,
			 'y_0':240,
			 'A':1,
			}),
	(ifft2,{}),
	(rigmor_sobel,{}),
	(fft2,{}),
	(fftshift,{}),
	(low_pass,{}),
	(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)

displayy = ( 
	'../img/test.jpg',
	[
	(display,{})],
	)

#Remember to add new procedures to this list
func_list = [smooth_test,sobel_test,epic_test]
