n = int(input('Primeiro número: '))
n1 = int(input('Segundo numero: '))

if n < n1:
    print('O {} é menor que {}'.format(n, n1))
elif n > n1:
    print('O {} é maior que {}'.format(n, n1))
else:
    print('Os numeros são iguais!')