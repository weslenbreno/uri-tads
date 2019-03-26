x = int(input())
y = int(input())

if x & 1 != 0 and y & 1 != 0:
	print(1)
elif x & 1 == 0 and y & 1 == 0:
	print(1)
else:
	print(0)