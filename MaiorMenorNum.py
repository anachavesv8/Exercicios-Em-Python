a = int(input('Primeiro Valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#verificando o menor numero
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando o maior numero

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))