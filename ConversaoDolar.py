val = float(input('Quanto dinheiro você tem na carteira? R$: '))
dolar = val / 5.11
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(val, dolar))