from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0

for c in range(1,8):

    nasc = int(input('Digite seu ano de nascimento: '))

    if anoAtual - nasc >= 18:
        maior += 1
    else: menor += 1

print(f'{maior} pessoas são maiores de idade',end=' ')
print(f' e {menor} são menores de idade')