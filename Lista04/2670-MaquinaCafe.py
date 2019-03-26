a = int(input())
b = int(input())
c = int(input())

a1 = 4*c + 2*b
a2 = 2*a + 2*c 
a3 = 4*a + 2*b

if a1 <= a2 and a1 <= a3:
	print(a1)
elif a2 <= a1 and a2 <= a3:
	print(a2)
else:
	print(a3)