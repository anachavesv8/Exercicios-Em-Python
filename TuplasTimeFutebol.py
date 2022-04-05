# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

colocação = ('Internacional', 'São Paulo', 'Flamengo', 'Atlético MG', 'Palmeiras',
             'Gremio', 'Fluminense', 'Corintians', 'Santos', 'Ceara', 'Red Bull Bragantino',
             'Athletico PR', 'Atlético GO', 'Vasco', 'Fortaleza', 'Bahia', 'Sport', 'Coritiba',
             'Góias', 'Botafogo')
print('-=' * 30)
print(colocação)
print('-=' * 30)
print(f'Os 5 primeiros colocados {colocação[:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados {colocação[-4:]}')
print('-=' * 30)
print(sorted(colocação))
print('-=' * 30)
print(f'O vasco está na: {colocação.index("Vasco")+1}ª posição')

