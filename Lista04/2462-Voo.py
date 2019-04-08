pa, cb, pb, ca = (
    map(lambda x: list(
        map(int, x.split(':'))) # Retorna uma lista com horas e minutos
        ,input().split())) # Retorna um iterador com os horários

# Calculando o tempo em minutos
t1 = pa[0] * 60 + pa[1] 
t2 = cb[0] * 60 + cb[1] 
t3 = pb[0] * 60 + pb[1] 
t4 = ca[0] * 60 + ca[1] 

# Calculando duração dos voos em minutos
primVoo = (t2 - t1) if (t2 - t1) > 0 else ((t2 - t1) + 1440)
segVoo = (t4 - t3) if (t4 - t3) > 0 else ((t4 - t3) + 1440)

# Calcula duração real dos voos em minutos
duracao = (primVoo + segVoo) // 2 - (720 if primVoo + segVoo > 1440 else 0)

#Calculando o fuso em minutos
resto = 1440 if primVoo - duracao > 720 else 0
fuso = primVoo - duracao - resto
    
print("{} {}".format(duracao, fuso//60))