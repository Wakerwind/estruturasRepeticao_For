
media = 0
count = 0
velho = 0

for c in range(1,5):

    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    media += idade

    if sexo == 'F' and idade < 20:
        count += 1

    if sexo == 'M' and idade > velho:

        velho = idade
        maisVelho = nome


print(f'A media das idades do grupo é = {media/4:.2f}')
print(f'Quantidade de mulheres com menos de 20 anos: {count}')
print(f'Nome do homem mais velho: {maisVelho}')