# 4 refrigerantes:
# coca (r0): 10 reais, 5 unidades
# guarana (r1): 8 reais,
# 3 unidades fanta (r2): 7 reais,
# 2 unidades uva (r3): 5 reais,
# 0 unidades
# O usuário seleciona um refri
# Se estiver zerado emite uma mensagem
# Se estiver no estoque pagamento (pode dar erro)
# desconta do estoque soma o valor no caixa libera o refri

print('''
[1] COCA
[2] GUARANA
[3] FANTA
[4] UVA
''')
refri = int(input('Selecione um refrigerante conforme menu acima: '))


if refri == 1:
  print('Tem em estoque, valor R$10')
  quant = int(input('Quantas unidade?: '))

  if quant > 5:
    print('Não possui quantidade suficiente em estoque. Apenas 5 unidades')
    quant = int(input('Quantas unidade?: '))
  est = 5 - quant
  valor = quant * 10
  print('O valor da compra é R${:.2f}'.format(valor))

if refri == 2:
  print('Tem em estoque, valor R$8')
  quant = int(input('Quantas unidade?: '))
  if quant > 3:
    print('Não possui quantidade suficiente em estoque. Apenas 3 unidades')
    quant = int(input('Quantas unidade?: '))
  est = 3 - quant
  valor = quant * 8
  print('O valor da compra é R${:.2f}'.format(valor))

if refri == 3:
  print('Tem em estoque, valor R$7')
  quant = int(input('Quantas unidade?: '))
  if quant > 2:
    print('Não possui quantidade suficiente em estoque. Apenas 2 unidades')
    quant = int(input('Quantas unidade?: '))
  est = 2 - quant
  valor = quant * 7
  print('O valor da compra é R${:.2f}'.format(valor))

if refri == 4:
  print('Não tem em estoque')