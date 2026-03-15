# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('DIGITE SUA PRIMEIRA NOTA: '))
n2 = float(input('DIGITE A SUA SEGUNDA NOTA?: '))
media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO')

elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')

elif media >= 7:
    print('APROVADO')
    