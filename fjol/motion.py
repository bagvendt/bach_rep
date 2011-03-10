from PIL import Image
import math
from constants import COLORLIST
import os

def main():
	BIN = 5
	for count in range(1,183):		
		infile = "test4/00000"
		if count < 10:
			infile += "00"
		elif count < 100:
			infile += "0"
		infile += str(count)+'.png'

		file,ext = os.path.splitext(infile)
		im = Image.open(infile)
		w,h = im.size
		w_diff = w % BIN
		h_diff = h % BIN
		w_new = w - w_diff
		h_new = h - h_diff
		box = (0, 0, w_new, h_new)
		newimg = im.crop(box)
		#new_file = open('temp.jpg','w')
		box_list = []
		wc = 0
		hc = 0
		pixels = newimg.load()
		for wi in range(0,w_new,BIN):
			for hi in range(0,h_new,BIN):
				sum_r = 0
				sum_g = 0
				sum_b = 0
				for i in range(wi,wi+BIN):
					for j in range(hi,hi+BIN):
						r,g,b =  pixels[i,j]
						sum_r += r
						sum_g += g 
						sum_b += b
				sum_r = sum_r / (BIN **2)
				sum_g = sum_g / (BIN **2)
				sum_b = sum_b / (BIN **2)
				for i in range(wi,wi+BIN):
					for j in range(hi,hi+BIN):
						newimg.putpixel((i,j), (sum_r,sum_g,sum_b))
		if count <= 9:
			newimg.save("test7/a00"+str(count)+ext)
		elif count <= 99:
			newimg.save("test7/a0"+str(count)+ext)
		else:
			newimg.save("test7/a"+str(count)+ext)

def nearest_color(color):
	r,g,b = color
	dist = []
	for candidate in COLORLIST:
		c_r,g_r,b_r = candidate
		cand_dist = math.sqrt(((r-c_r) ** 2) + ((g-g_r) **2) + ((b-b_r) ** 2))
		dist.append(cand_dist)
	a = COLORLIST[dist.index(min(dist))]
	return a
if __name__ == '__main__':
	main()
