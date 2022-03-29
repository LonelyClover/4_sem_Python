f = open('med_research.txt', 'r')
data = [line.strip().split(' ') for line in f.readlines()]
f.close()

output = [ [elem[i] for elem in data] for i in range(len(data[0]))]	

f = open('output.txt', 'w')
for elem in output:
	print(*elem, sep=' ', file=f)

f.close()
