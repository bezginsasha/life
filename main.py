from PIL import Image

arr = []

def is_there_life(pixel):
	"""
	function get pixel from image
	if this pixel is black, function returns true
	else return false
	"""
	return pixel[0] == 0

def read_image_to_array():
	"""
	function read all pixels in default.png image
	and every black pixel understands as live cell
	then function create matrix list of boolean and returns it
	"""
	img = Image.open('default.png')
	res_arr = []

	for y in range(img.height):
		res_arr.append([])

		for x in range(img.width):
			pixel = img.getpixel((x,y))
			res_arr[y].append(is_there_life(pixel))
	return res_arr
