n = int(input())
first = 0
sec = 1
space = ' '
for i in range(1, n+1):
  if(i == n):
    space = '\n'
  if i == 1:
    print(0, end=space)
  elif i == 2:
    print(1, end=space)
  else:
    prox = first + sec
    first = sec  
    sec = prox
    print(prox, end=space)