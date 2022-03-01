# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LA CHAVES'))
valor = float(input('\nPreço das compras R$: '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro
[ 2 ] à vista no Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('\nQual a sua opção? '))

if opção == 1:
    val = valor - (valor * 0.10)
    print('\nSua compra de R${:.2f}, vai custar no final R${:.2f}. '.format(valor, val))
elif opção == 2:
    val = valor - (valor * 0.05)
    print('\nSua compra de R${:.2f}, vai custar no final R${:.2f}. '.format(valor, val))
elif opção == 3:
    val = valor / 2
    print('Sua compra de {}, será parcelada em 2x de R${:.2f} SEM JUROS'.format(valor, val))
    print('\nSua compra de R${:.2f}, vai custar no final R${:.2f}. '.format(valor, val))
elif opção == 4:
    val = valor + (valor * 0.20)
    parc = int(input('Quantas parcelas? '))
    valpar = val / parc
    print('Sua compra de R${:.2f}, será parcelada em {}x de R${:.2f} COM JUROS'.format(valor, parc, valpar))
    print('\nSua compra de R${:.2f}, vai custar no final R${:.2f}. '.format(valor, val))
else:
    print('Opção Inválida, tente novamente!')
