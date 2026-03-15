# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

titulo = 'O COMPARADOR'

print('*-*'*20)
print(f'\033[1;34m{titulo:^60}\033[m')
print('*-*'*20)

n1 = int(input('\n\033[1;35mESCOLHA UM NÚMERO INTEIRO: \033[m'))
n2 = int(input('\n\033[1;35mESCOLHA OUTRO NÚMERO INTEIRO: \033[m'))

if n1 > n2:
    print('\n\033[1mO PRIMEIRO VALOR É MAIOR!\n')

elif n2 > n1:
    print('\n\033[1mO SEGUNDO VALOR É MAIOR!\n')

else:
     print('\n\033[1mNÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.\n')