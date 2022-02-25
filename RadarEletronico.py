#Crie um programa que leia a velocidade de um carro
#se ele ultrapassar 80KM/h mostre uma msg dizendo que foi multado
#a multa vai custar R$7,00 por cada KM acima do limite

km = float(input('Qual a velocidade? '))

if km > 80:
    print('Você foi MULTADO!!! Você excedeu o limite permitido que é de 80km/h')
    multa = (km - 80) * 7
    print('O valor da multa é R${:.2f}'.format(multa))
else:
    print("Você está no limite permitido! Dirija com Segurança!")