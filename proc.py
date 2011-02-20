from functions import *

test1 = ( 
	'../img/celle1.png',
	[(fft2,{}),
	(abs_func,{}),
	(gauss,{'value':0.0044,}),
	(fftshift,{}),
	(display,{})],
	)

test2 = ( 
	'../img/celle1.png',
	[(fft2,{}),
	(abs_func,{}),
	(display,{})],
	)

#Remember to add new procedures to this list
func_list = [test1,test2]
