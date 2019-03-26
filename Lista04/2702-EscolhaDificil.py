a, b, c = map(int, input().split())
a1, b2, c2 = map(int, input().split())

soma = 0
if(a1 > a):
	soma += a1-a
if b2 > b:
	soma+= b2-b
if c2 > c:
	soma += c2-c

print(soma)