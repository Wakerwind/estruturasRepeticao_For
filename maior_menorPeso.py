maior = 0
menor = 0

for c in range(1,6):
    peso = float(input(f'Digite o pesoa da {c} pessoa: '))

    if c == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'{maior:.2f} é o maior peso e {menor:.2f} é o menor')