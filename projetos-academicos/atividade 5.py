gênero=input('Informe o gênero (homem ou mulher):').strip().lower()
altura=float(input('Qual a sua altura?'))
mulher=(62.1*altura)-44.7
homem=(72.7*altura)-58
if gênero.lower()=='mulher':
    print('O seu peso ideal é',mulher)
elif gênero.lower()=='homem':
    print('O seu peso ideal é',homem)
else:
    print('Gênero inválido.')
