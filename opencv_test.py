import cv
def main():
	imgfile = "../img/celle1.png"
	img = cv.LoadImage(imgfile, 1)
	cv.NamedWindow("test",1)
	cv.ShowImage("test",img)
	#dst = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 3);
	#storage = cv.Create(1, 2, cv.CV_32FC3)
	w,h = cv.GetSize(img)
	print w,h
	storage = cv.CreateMat(1, h*w, cv.CV_32FC3)	
	gray = cv.CreateImage(cv.GetSize(img), 8, 1)
	edges = cv.CreateImage(cv.GetSize(img), 8, 1)
	cv.CvtColor(img, gray, cv.CV_BGR2GRAY)
	cv.Canny(gray, edges, 101, 250, 3)
			

	cv.SaveImage("test.jpg" ,edges);

if __name__ == '__main__':
	main()
