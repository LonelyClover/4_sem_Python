f = open('poe_unpublished.txt', 'r')
data = [line.strip().split(' ') for line in f.readlines()]
f.close()

data.sort(key=len)
for elem in data:
	elem.sort(key=len)

f = open('poe_decode_attempt.txt', 'w')
for elem in data:
	print(*elem, sep=' ', file=f)

f.close()
