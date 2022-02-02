aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = int(input(f'A média de {aluno["nome"]} é: '))


if aluno['média'] >= 5:
    print('A situação da aluno é igual a Aprovação')

if aluno['média'] < 5:
    print('A situação da aluno é igual a Reprovação')



