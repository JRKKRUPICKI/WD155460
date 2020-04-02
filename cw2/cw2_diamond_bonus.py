def diamond(width=5, symbol='o'):
	for level in range(1, width+2, 2):
		print(f'{symbol*level:^{width}}')
	for level in range(1, width-2, 0, -2):
		print(f'{symbol*level:^{width}}')