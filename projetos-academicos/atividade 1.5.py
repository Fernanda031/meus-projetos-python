a=float(input('Digite o valor da reta A:'))
b=float(input('Digite o valor da reta B:'))
c=float(input('Digite o valor da reta C:'))
if a+b<c or a+c<b or b+c<a:
    print('Essas retas não podem formar um triângulo.')
elif a==b==c:
    print('Essas retas formam um triângulo equilátero.')
elif a==b or a==c or b==c:
    print('Essas retas formam um triângulo isósceles.')
else:
    print('Essas retas formam um triângulo escaleno.')