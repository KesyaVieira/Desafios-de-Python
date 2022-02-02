from random import randint
lista = list()
sorteios = list()
jogos = int(input('Quantos jogos você quer fazer? '))
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
           lista.append(num)
           cont += 1
        if cont >= 6:
           break
    lista.sort()
    sorteios.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(sorteios):
    print(f'jogo {i+1}: {l}')
