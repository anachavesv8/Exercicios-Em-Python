n = int(input('Digite um numero inteiro: '))
n1 = int(input('Digite segundo valor: '))
print('''Escolha uma das operação:
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO''')

opção = int(input('Sua opção: '))
if opção == 1:
    print('{} + {} = {}'.format(n, n1, (n+n1)))
elif opção == 2:
    print('{} - {} = {}'.format(n, n1, (n-n1)))
elif opção == 3:
    print('{} * {} = {}'.format(n, n1, (n*n1)))
elif opção == 4:
    print('{} / {} = {}'.format(n, n1, (n//n1)))
else:
    print('Opção invalida.Tente novamente!!')