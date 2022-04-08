senha = ''
nascimento = ''
nome = str(input('Nome: ')).upper().strip()
nome1 = any(chr.isdigit() for chr in nome)
while True:
    if nome1 == False or nome1 == '':
        break
    print('Erro! Ou contem numeros ou esta vazio')
    nome = str(input('Nome: ')).upper().strip()
    nome1 = any(chr.isdigit() for chr in nome)
nascimento = str(input('Ano nascimento [aaaa]:'))
while True:
    if len(nascimento) == 4:
        break
    print('Erro! Formato invalido, por favor digite novamente!')
    nascimento = str(input('Ano nascimento [aaaa]:'))
senha = nascimento[2:] + nome[:2] + nascimento[:2] + nome[2:]
print(senha)