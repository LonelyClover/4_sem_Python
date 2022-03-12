with open('input.txt', 'r') as f:
	for line in f.readlines():
		words = line.strip().split(' ')	
		print(' '.join(map(lambda word: word[::-1], words)))
