b, a = map(int, input().split())


if b == 1:
	print('Total: R$ {:.2f}'.format(a*4.0))
elif b == 2:
	print('Total: R$ {:.2f}'.format(a*4.50))
elif b == 3:
	print('Total: R$ {:.2f}'.format(a*5.00))
elif b == 4:
	print('Total: R$ {:.2f}'.format(a*2.00))
else:
	print('Total: R$ {:.2f}'.format(a*1.50))