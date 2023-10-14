#A estrutura for é usada quando queremos repetir algo por um certo número de vezes
# ele vai repetir 7 vezes esse bloco, ele conto o número anterior ao final do range()

for c in range(1,8):

    print('Bate...',end='')

print(' Espada forjada!')

#A variável c pega o valor do número do looping atual
# contagem regressiva de 10 até 1 decrementando em -1

for c in range(10,0,-1):

    print(f'{c}')

print('Decolar!')

#Conta de 2 até 10 pulando de dois em dois

print('Estes são os números pares entre 0 e 10: ')
for c in range(2,11,2):
    print(f'{c}')


#Podemos usar outras variáveis para definir o range do for

level = int(input('Digite quantos leveis você quer subir sua arma: '))

for c in range(1,level+1):

    print('Arma level ',c)











