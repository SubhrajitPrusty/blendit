import sys
from PIL import Image

if len(sys.argv) < 2:
	print("No arguments detected. Exiting.")
else:
	imgname = sys.argv[1]

	img = Image.open(imgname)

	data = list(img.getdata())

	rsum, gsum, bsum = 0,0,0
	pixels = len(data)

	for pixel in data:
		rsum+=pixel[0]
		gsum+=pixel[1]
		bsum+=pixel[2]

	ravg = rsum//pixels
	gavg = gsum//pixels
	bavg = gsum//pixels

	avg_RGB = (ravg,gavg,bavg)

	new_im = Image.new('RGB',(100,100),avg_RGB)
	new_im.show()