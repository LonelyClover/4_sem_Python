with open('input.txt', 'r') as f:
	for line in f.readlines():
		print(' '.join([word for i, word in enumerate(line.strip().split(' ')) if i % 2 == 0]))
