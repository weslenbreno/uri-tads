t = list(map(int, input().split()))
t.sort(reverse=True)
a, b, c, d = t;

c1 = ((abs(b - c) < a < b + c) and 
	 (abs(a - c) < b < a + c) and
	 (abs(a - b) < c < a + b))

a = d;
c2 = ((abs(b - c) < a < b + c) and 
	 (abs(a - c) < b < a + c) and
	 (abs(a - b) < c < a + b))

if c1 or c2:
	print('S')
else:
	print('N')