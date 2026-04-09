# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('FAÇA A SUA ESCOLHA!')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
eu = int(input('DECISÃO: '))
comp = random.choice([1, 2, 3])

if eu == comp:
    print('DROGA! FOI EMPATE!')

elif eu == 1 and comp == 2:
    print('HÁ! EU GANHEI! ESCOLHI PAPEL!')

elif eu == 1 and comp == 3:
    print('DROGA! EU PERDI! EU ESCOLHI TESOURA!')

elif eu == 2 and comp == 1:
    print('DROGA! EU PERDI! EU ESCOLHI PEDRA!')

elif eu == 2 and comp == 3:
    print('HÁ! EU GANHEI! EU ESCOLHI TESOURA!')

elif eu == 3 and comp == 1:
    print('HÁ! EU GANHEI! EU ESCOLHI PEDRA!')

elif eu == 3 and comp == 2:
    print('DROGA! EU PERDI! EU ESCOLHI PAPEL!')

else:
    print('SELECIONE UM NÚMERO VÁLIDO.')


