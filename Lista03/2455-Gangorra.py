a, b, c, d = map(int, input().split())

if a*b == c*d:
	print('0')
elif a*b > c*d:
	print('-1')
else:
	print('1')
