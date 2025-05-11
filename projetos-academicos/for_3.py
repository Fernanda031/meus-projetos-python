ct=0
soma=0
for numero in range(1,11,1):
    dobro=numero*2
    print(dobro)
    ct=ct+1
    soma=soma+numero
    media=soma/ct
print('Soma: ',soma)
print('Média: ',media)