#primeira opção:

n =  int(input('Digite um valor: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

#segunda opção:
n =  int(input('Digite um valor: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'. format(n, (n-1), (n+1)))