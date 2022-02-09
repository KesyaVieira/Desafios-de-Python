
def maior(* num):
    cont = maior = 0
    print('Os valores informados são: ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' <= Dentre esses, o maior valor informado foi {maior}. ')


maior(9, 5, 3, 1, 2, 27, 17, 101)
