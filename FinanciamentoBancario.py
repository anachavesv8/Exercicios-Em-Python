casa = float(input('Valor da casa: R$'))
salario = float(input('Qual sua renda? R$'))
tempo = int(input('Quantos meses para pagar? '))
prestação = casa / tempo
minimo = salario * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo), end='')
print('\nA prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO!!')
