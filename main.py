from PIL import Image
import curses

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

def get_char_to_display(in_value):
	"""
	if input value is true it means need to draw element
	and therefore function returns # symbol
	else function return space
	"""
	return '#' if in_value else ' '

def draw_current_arr(arr):
	"""
	function to draw arr to console
	i add try catch because in borders
	function often stdscr.addstr crashes
	"""
	for y, y_value in enumerate(arr):
		for x, x_value in enumerate(y_value):
			try:
				stdscr.addstr(y,x,get_char_to_display(x_value))
			except curses.error:
				pass

	stdscr.refresh()

def get_count_life_neighbor(arr, x, y, max_x, max_y):
	"""
	function lools at neighbors and
	returns count of True neighbors
	"""
	res_count = 0

	if x > 0 and y > 0:
		if arr[y-1][x-1]:
			res_count += 1

	if y > 0:
		if arr[y-1][x]:
			res_count += 1

	if y > 0 and x < max_x:
		if arr[y-1][x+1]:
			res_count += 1

	if x > 0:
		if arr[y][x-1]:
			res_count += 1;

	if x < max_x:
		if arr[y][x+1]:
			res_count += 1

	if y < max_y and x > 0:
		if arr[y+1][x-1]:
			res_count += 1

	if y < max_y:
		if arr[y+1][x]:
			res_count += 1

	if y < max_y and x < max_x:
		if arr[y+1][x+1]:
			res_count += 1

	return res_count

def life(arr):
	"""
	function looks at input array, copy it to res_array
	and change res_array with rules of game
	"""
	res_arr = arr
	max_x = len(arr[0]) - 1
	max_y = len(arr) - 1

	for y, y_value in enumerate(arr):
		for x, x_value in enumerate(y_value):
			neighb_count = get_count_life_neighbor(arr, x, y, max_x, max_y)
			if x_value:
				if neighb_count < 2 or neighb_count > 3:
					res_arr[y][x] = False
			else:
				if neighb_count == 3:
					res_arr[y][x] = True
	return res_arr
