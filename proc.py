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
test3 = ( 
	'../img/test.jpg',
	[
	(fft2,{}),
	#(test_func,{}),
	(ifft2,{}),
	(display,{})],
	)

test4 = ( 
	'../img/test.jpg',
	[
	(fft2,{}),
	(abs_func,{}),
	(fftshift,{}),
	#(gauss,{'value':0.5,}),
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
func_list = [test1,test2,test3,test4,displayy]
