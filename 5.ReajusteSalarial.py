# Reajuste salarial: As empresas @.com resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o salario atual do funcinario R$ '))

if salario <= 280:
    a1 = salario + (salario * 0.20)
    a11 = a1 - salario
    print('O salario do funcionario era de {:.2f} e agora será de {:.2f}. O percentual utilizado é 20%, acrescentando {:.2f}'.format(salario, a1, a11))

elif salario > 280 and salario <= 700:
    a2 = salario + (salario * 0.15)
    a21 = a2 - salario
    print('O salario do funcionario era de {:.2f} e agora será de {:.2f}. O Percentual utilizado é 15%, ascrescentando {:.2f}'.format(salario, a2, a21))

elif salario > 700 and salario <= 1500:
    a3 = salario + (salario * 0.10)
    a31 = a3 - salario
    print('O salario do funcionario era de {:.2f} e agora será de {:.2f}. O Percentual utilizado é 10%, ascrescentando {:.2f}'.format(salario, a3, a31))

else:
    a4 = salario + (salario * 0.05)
    a41 = a4 - salario
    print('O salario do funcionario era de {:.2f} e agora será de {:.2f}. O Percentual utilizado é 5%, ascrescentando {:.2f}'.format(salario, a4, a41))