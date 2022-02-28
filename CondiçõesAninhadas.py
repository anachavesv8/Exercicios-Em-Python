nome = str(input('Qual seu nome? ')).capitalize(). strip()
if nome == 'Ana':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome == 'Paula' or nome == 'Fabiana' or nome == 'Natalia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum!')
print('Tenho um bom dia {}!!!'.format(nome))