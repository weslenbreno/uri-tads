n = int(input())

for i in range(n):
  num = int(input())
  isPrime = True
  for idx in range(2, num):
    if num % idx == 0:
      isPrime = False
      break
  if isPrime:
    print("{} eh primo".format(num))
  else:
    print("{} nao eh primo".format(num))