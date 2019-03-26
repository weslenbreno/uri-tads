d = int(input())
a, b, c = map(int, input().split())

if d <= a and d <= b and d <= c:
	print('S')
else:
	print('N')