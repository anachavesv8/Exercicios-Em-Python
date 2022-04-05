# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferido', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 3.99,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #configurado centralizado
print('-' * 40)
for i in range(0, len(listagem)): #0 considerando posição, no comprimento da tupla
    if i % 2 == 0:   #irá verificar se a posição é par ou impar para conseguir alinhar na tabulação
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:.>7.2f}') #configurar o valor configurado em 7 espaços em numero float
