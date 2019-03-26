x = int(input())

if x <= 10:
	print('7')
elif x <= 30:
	acumulo30 = x - 10;
	print(7 + acumulo30)
elif x <= 100:
	acumulo100 = x - 30;
	print(7 + 20 + acumulo100*2)
else:
	print(7 +  20 + 140 + (x - 100)*5)