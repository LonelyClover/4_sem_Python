f = open('weights.txt', 'r')
data = [line.strip().split(' ') for line in f.readlines()]
f.close()

data.sort(key=lambda elem: float(elem[1]), reverse=True)

f = open('team.txt', 'w')
for elem in data[::2] + data[1::2]:
	print(*elem, sep=' ', file=f)

f.close()
