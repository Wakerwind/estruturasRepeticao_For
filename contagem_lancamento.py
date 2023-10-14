#Contagem regressiva para o lançamento de fogos

from time import sleep


#O sleep faz ter um delay de 1 segundo no programa


for c in range(10,-1,-1):
    print(c)
    sleep(1)

print('Os fogos foram lançados!')