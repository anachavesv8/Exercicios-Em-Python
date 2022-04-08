# Crie um programa que leia nome, sexo e idade de várias
# pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
galera = []
pessoa = {}
soma = 0
media = 0

while True: #cadastrar as pessoas no dicionario pessoa
    pessoa.clear() #depois de acionar a pessoa, limpar para a inclusão da proxima
    pessoa['nome'] = str(input('Nome: ')).upper().strip()
    while True: #caso digitar errado, acuse erro
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()[0].strip()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) #adicionando a pessoa (dict) na lista
    while True:
        cont = str(input('Deseja continuar? [s/n]')).upper()
        if cont in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if cont == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idades é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('>>> ENCERRADO <<<')

