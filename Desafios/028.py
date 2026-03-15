# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
import emoji

titulo = 'O JOGO DA ADIVINHAÇÃO'

numC = randint(0,5)

print('-=-' * 30)
print(emoji.emojize(f'\033[4;36;45m:glowing_star:{titulo:^86}:glowing_star:'))
print('-=-' * 30)

numH = int(input('\nEm qual número de 0 a 5 eu estou pensando?...'))
print('\nPROCESSANDO...')
sleep(1.5)

if numH == numC:
    print('\nEu não acredito! Pensamos no mesmo número!', numC)

else:
    print('\nHAHAHAHA! Pensamos em número diferentes...MELHORE!\n')
