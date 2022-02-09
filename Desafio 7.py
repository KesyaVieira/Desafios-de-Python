
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos você ainda não pode votar!'
    elif 16 <= idade < 18 or idade > 65:
        return f' Com {idade} anos o voto é opcional!'
    else:
        return f'Com {idade} anos o voto é obrigatório!'


nasc = int(input('Em que ano você nasceu? '))

print(voto(nasc))
