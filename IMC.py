# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal
# (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura (metros): '))
peso = float(input('Digite seu peso (KG): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso!!'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.1f}, você está no peso Ideal!'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.1f}, você está com sobrepeso'.format(imc))
elif imc <=40:
    print('Seu IMC é {:.1f}, você está Obesidade!'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está com obesidade Morbida!'.format(imc))
