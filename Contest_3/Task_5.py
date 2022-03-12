import itertools as it

with open('studygroup.txt', 'r') as f:
	names = f.readline().strip().split(' ')
	for triple in it.combinations(names, 3):
		print('1: ' + triple[0] + ' 2: ' + triple[1] + ' 3: ' + triple[2])
