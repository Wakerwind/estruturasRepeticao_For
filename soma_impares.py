#Soma dos números inpares entre 1 e 500 que são múltiplos de 3
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma+=c
print(f'A soma é: {soma}')