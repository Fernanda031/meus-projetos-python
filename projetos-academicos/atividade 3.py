x1=float(input('Digite o valor da abscissa x1 do plano cartesiano:'))
y1=float(input('Digite o valor da ordenada y1 do plano cartesiano:'))
x2=float(input('Digite o valor da abscissa x2 do plano cartesiano:'))
y2=float(input('Digite o valor da ordenada y2 do plano cartesiano:'))
distância=x2-x1
d=y2-y1
h=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
h=h**(1/2)
if y1==y2:
    print('O valor da distância entre os pontos P e Q é igual a',distância)
elif x1==x2:
    print('O valor da distância entre os pontos P e Q é igual a',d)
else:
    print('O valor da distância entre os pontos P e Q é igual a',h)

