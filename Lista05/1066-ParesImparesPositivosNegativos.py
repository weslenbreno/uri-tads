par = impar = negativos = positivos = 0

for i in range(5):
    n = int(input())
    if(n > 0):
        positivos+=1
    elif n < 0:
        negativos+=1

    if(n % 2 == 0):
        par +=1
    else:
        impar += 1


print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivos))
print("{} valor(es) negativo(s)".format(negativos))