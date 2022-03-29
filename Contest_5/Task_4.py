f = open('the_calls.txt', 'r')
data = [line.strip().split('\t') for line in f.readlines()]
f.close()

data.sort(key=lambda elem: elem[2]) 
dataA = [elem for elem in data if elem[2] == 'A']
dataA.sort(key=lambda elem: int(elem[1]), reverse=True)
dataB = [elem for elem in data if elem[2] == 'B']
dataB.sort(key=lambda elem: int(elem[1]), reverse=True)

f = open('calls.txt', 'w')
for elem in dataA + dataB:
	print(*elem, sep='\t', file=f)

f.close()
