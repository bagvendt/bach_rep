from proc import *
import sys

def main():
	arg = sys.argv 
	if len(arg) != 2:
		print 'NO WAY'
		sys.exit()
	
	a = int(arg[1])
	if a < 0 or a >= len(func_list):
		print 'Not in list'
		sys.exit()
	run(func_list[a])

def run(arg):
	image,funcs = arg
	(img,env) = setup(image,())
	for func,args in funcs:
		(img,env) = func.__call__(img=img,env=env ,**args )
	
if __name__ == '__main__':
	main()

