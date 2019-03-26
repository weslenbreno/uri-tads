a, b = map(int, input().split())

if (b - a) == 0:
	print('O JOGO DUROU 24 HORA(S)')
elif b < a:
	print('O JOGO DUROU {} HORA(S)'.format((24+b) -a))
else:
	print('O JOGO DUROU {} HORA(S)'.format(b-a))