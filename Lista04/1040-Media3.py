a, b, c, d = map(float, input().split())
media = ( (2*a) + (3*b) + (4*c) + d ) / 10;

print("Media: {:.1f}".format(media));

if media >= 7.0:
	print("Aluno aprovado.")
elif media < 5.0:
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	e = float(input())
	print("Nota do exame: {:.1f}".format(e))
	media = (media + e) / 2.0;

	if(media >= 5.0):
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")

	print("Media final: {:.1f}".format(media))