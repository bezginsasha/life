from PIL import Image

arr = []

def is_there_life(pixel):
	"""
	function get pixel from image
	if this pixel is black, function returns true
	else return false
	"""
	return pixel[0] == 0
