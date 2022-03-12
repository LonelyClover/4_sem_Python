with open('input.txt', 'r') as f:
	print(''.join(filter(lambda line: 'ё' in line, f.readlines())), end='')
