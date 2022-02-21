n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

soma = n1 + n2 + n3 + n4
media = soma / 4

print('A média entre {}, {}, {},{} é {:.2f}'.format(n1, n2, n3, n4, media))

if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')