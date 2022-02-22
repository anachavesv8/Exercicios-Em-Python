
# Conversor de moedas: Crie um programa que solicite um um valor em real ao usuário e converta esse valor, para:
# DOLAR
# EURO
# LIBRA ESTERLINA
# DÓLAR CANADENSE
# PESO ARGENTINO
# PESO CHILENO
# Para esse exercício você precisará realizar uma pesquisa para saber a cotação de cada moeda em real. Mostrar o resultado no formato U$9999.99

valor = float(input('Qual o valor? '))

dolar = 5.17 * valor
dolar1 = round(dolar, 2)
euro = 5.88 * valor
euro1 = round(euro, 2)
libra = 7.05 * valor
libra1 = round(libra, 2)
dolarc = 4.07 * valor
dolarc1 = round(dolarc, 2)
peso = 0.049 * valor
peso1 = round(peso, 2)
chi = 0.0065 * valor
chi1 = round(chi, 2)
print('Em dolar será U$ ', dolar1)
print('Em Euro será U$ ', euro1)
print('Em Libra Esterlina será U$ ', libra1)
print('Em Dolar Canadense será U$ ', dolarc1)
print('Em Peso Argentino será U$ ', peso1)
print('Em Peso Chinelo será U$ ', chi1)