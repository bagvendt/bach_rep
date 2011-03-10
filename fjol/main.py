from PIL import Image

def main():
	a = Image.open('../img/cm.jpg')
	pixels = a.load()
	w,h = a.size
	BIN = 50
	print pixels
	for wi in range(w):
		for hi in range(h):
			print pixels[wi,hi]

if __name__ == '__main__':
	main()
