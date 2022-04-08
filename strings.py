senha = ''
nascimento = ''
nome = str(input('Nome: ')).upper().strip()
nome1 = nome.isdigit()

#if nome1 == False or nome1 == '':
    print('Erro! Ou contem numeros ou esta vazio')
nascimento = str(input('Ano nascimento [aaaa]:'))
if len(nascimento) > 4:
    print('Erro! Formato invalido, por favor digite novamente!')
else:
    senha = nascimento[2:] + nome[:2] + nascimento[:2] + nome[2:]
print(senha)