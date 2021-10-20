from PIL import Image, ImageFilter
import networkx as nx

def pixels_equal(pix1, pix2):
	return pix1 == pix2

def pixels_connected(image, tcoord, pos_a, pos_b, compare = pixels_equal):
	# -1 unsearched, 0 not connected, 1 connected
	state = [[-1] * 5 for _ in range(5)]

	def depth_first(pos):
		if pos == pos_b:
			return True

		pix_a = image.getpixel((tcoord[0] + pos[0], tcoord[1] + pos[1]))
		nxbours = [(pos[0] - 1, pos[1] + 0), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
		nxbours = [nx for nx in nxbours if nx[0] >= 0 and nx[0] < 5]
		nxbours = [nx for nx in nxbours if nx[1] >= 0 and nx[1] < 5]
		nxbours = [nx for nx in nxbours if state[nx[0]][nx[1]] == -1]
		for nx in nxbours:
			pix_b = image.getpixel((tcoord[0] + nx[0], tcoord[1] + nx[1]))
			if pixels_equal(pix_a, pix_b):
				state[nx[0]][nx[1]] = 1
			else:
				state[nx[0]][nx[1]] = 0

		for nx in nxbours:
			if state[nx[0]][nx[1]] == 1 and depth_first(nx):
				return True

		return False

	return depth_first(pos_a)

def tile_from_bitmap(image, tcoord):
	# just testing func atm
	print(tcoord)
	if pixels_connected(image, tcoord, (1, 4), (3, 0)):
		print("BL connected to TR")
	else:
		print("BL NOT connected to TR")
	
	return None

def all_tiles_from_bitmap(filename = "tiles.png", w = 7, h = 12):
	im = Image.open(filename)
	return [tile_from_bitmap(im, (x * 5, y * 5)) for x in range(w) for y in range(h)]
