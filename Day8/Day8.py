import matplotlib.pyplot as plt


def first_star(pixels, img_width, img_height):
	fewest_0_digits = float('inf')
	value = -1
	
	for i in range(0, len(pixels)+1-img_width*img_height, img_width*img_height):
		layer = pixels[i:i+img_width*img_height]
		number_zeros = layer.count('0')
		if number_zeros < fewest_0_digits:
			fewest_0_digits = number_zeros
			value = layer.count('1') * layer.count('2')
	return value

def second_star(pixels, img_width, img_height):
	layers = []
	for i in range(0, len(pixels)+1-img_width*img_height, img_width*img_height):
		layers.append(pixels[i:i+img_width*img_height])
	
	image = list(zip(*layers))
	
	for i, layer in enumerate(image):
		transparent = True
		for j, pixel in enumerate(layer):
			if pixel != '2':
				image[i] = pixel
				transparent = False
				break
		if transparent == True:
			image[i] = '2'
	
	img_matrix = []
	for i in range(0, len(image)-1, img_width):
		img_matrix.append(image[i:i+img_width])

	for i in range(len(img_matrix)):
		for j in range(len(img_matrix[0])):
			if img_matrix[i][j] == '0': #black
				img_matrix[i][j] = 0
			elif img_matrix[i][j] == '1': #white
				img_matrix[i][j] = 255
			elif img_matrix[i][j] == '2': #transparent
				img_matrix[i][j] = 128
	
	return img_matrix

if __name__ == '__main__':
	with open('input.txt') as f:
		pixels = f.read().strip()
	
	print(first_star(pixels, 25, 6))
	
	plt.imshow(second_star(pixels, 25, 6))
	plt.show()
