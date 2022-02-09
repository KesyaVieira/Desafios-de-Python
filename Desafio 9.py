def leiaint(msg):
    oi = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            oi = True
        else:
            print('Erro! Digite um número válido! ')
        if oi:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
