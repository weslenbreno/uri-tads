media = 0.0
positivos = 0
for i in range(6):
    n = float(input())
    if(n > 0):
        positivos+=1
        media += n

print("{} valores positivos".format(positivos))
print("{:.1f}".format(media / positivos))