frase = str(input('Digite uma frase: ')).strip().lower()

frase = frase.split(' ')

frase = ''.join(frase)
inverso = ''
for c in range(len(frase) - 1, -1, -1):

    inverso = inverso + frase[c]

if inverso == frase:
    print(f'{inverso.title()} é um palíndromo')
else: print(f'{inverso.title()} não é um palíndromo')