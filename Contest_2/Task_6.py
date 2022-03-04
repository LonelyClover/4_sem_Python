separators = "()- "
str = input()
for s in separators:
	list = str.split(s)
	str = ''.join(list)
print(str)
