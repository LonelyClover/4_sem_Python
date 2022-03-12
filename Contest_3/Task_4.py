with open('input.txt', 'r') as in_f, open('output.txt', 'w') as out_f:
	lines = [line.strip() for line in in_f.readlines()]
	N = int(lines[0])
	for pair in zip(lines[1:N+1], lines[N+1:2*N+1]):
		out_f.write('\t'.join(pair) + '\n')
