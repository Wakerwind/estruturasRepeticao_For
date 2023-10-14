#Somatoria de seis números pares
soma = 0

for c in range(1,7):

    num = int(input('Digite um número: '))

    if num % 2 == 0:
        soma+=c

print(f'A soma dos pares é = {soma}')