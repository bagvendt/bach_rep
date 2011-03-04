from functions import *
from leg import *

smooth_test = ( 
	'../img/celle1.png',
	[(fft2,{}),
	(fftshift,{}),
	(gaussian_blur,{'sigma':15,
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
	'../img/celle1.png',
	[(fft2,{}),
	(fftshift,{}),
	(gaussian_blur,{'sigma':15,
			}),
	(ifft2,{}),
	(rigmor_sobel,{}),
	#(fft2,{}),
	#(low_pass,{}),
	#(ifft2,{}),
	(abs_func,{}),
	(display,{})],
	)

displayy = ( 
	'img/test.jpg',
	[
	(display,{})],
	)

mexican_test = ( 
	'../img/celle1.png',
	[(tondcheck,{}),
	(display,{})],
	)

#Remember to add new procedures to this list
func_list = [smooth_test,sobel_test,epic_test,mexican_test]
