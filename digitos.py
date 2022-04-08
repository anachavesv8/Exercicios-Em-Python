palavra = str(input('Digite uma palavra: ')).upper().strip()

if len(palavra) > 6 or palavra == '':
    print('Erro')
for k, v in enumerate(palavra):
    print(f' {k}º caracter da palavra é {v}')