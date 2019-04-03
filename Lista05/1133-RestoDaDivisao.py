x = int(input())
y = int(input())

for i in range(int(min(x, y))+1, int(max(x,y))):
  if i % 5 == 2 or i % 5 == 3:
    print(i)