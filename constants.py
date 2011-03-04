import numpy
import math
MEXHAT_LARGE = numpy.array([
[0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,0,0,0],
[0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0],
[0,0,-1,-1,-1,-2,-3,-3,-3,-3,-3,-2,-1,-1,-1,0,0],
[0,0,-1,-1,-2,-3,-3,-3,-3,-3,-3,-3,-2,-1,-1,0,0],
[0,-1,-1,-2,-3,-3,-3,-2,-3,-2,-3,-3,-3,-2,-1,-1,0],
[-1,-1,-3,-3,-3,0,4,10,12,10,4,0,-3,-3,-3,-1,-1],
[-1,-1,-3,-3,-2,2,10,18,21,18,10,2,-2,-3,-3,-1,-1],
[-1,-1,-3,-3,-3,4,12,21,24,21,12,4,-3,-3,-3,-1,-1],
[-1,-1,-3,-3,-2,2,10,18,21,18,10,2,-2,-3,-3,-1,-1],
[-1,-1,-3,-3,-3,0,4,10,12,10,4,0,-3,-3,-3,-1,-1],
[0,-1,-1,-2,-3,-3,-3,-2,-3,-2,-3,-3,-3,-2,-1,-1,0],
[0,0,-1,-1,-2,-3,-3,-3,-3,-3,-3,-3,-2,-1,-1,0,0],
[0,0,-1,-1,-1,-2,-3,-3,-3,-3,-3,-2,-1,-1,-1,0,0],
[0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0],
[0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,0,0,0],
])

MEXHAT_SMALL = numpy.array([[0,0,-1,0,0],
							[0,-1,-2,-1,0],
							[-1,-2,16,-2,-1],
							[0,-1,-2,-1,0],
							[0,0,-1,0,0]
							])

PI_4 = math.pi/4
