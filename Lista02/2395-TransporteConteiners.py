a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
cima = int(z/c)
comp = int(y/b)
larg = int(x/a)
print(cima * comp * larg)