# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from emoji import emojize
from time import sleep

print('\n')
print('-'*60)
print('|', ' ' * 22, 'VELOCÍMETRO', ' ' * 21, '|')
print('-'*60)

print('VRUMM! <<<<')
print('\nPROCESSANDO...')
sleep(1.5)

velo = float(input('\nQuantos Km/h estava o carro?: '))

if velo > 80:
    print(emojize('\nVocê foi MULTADO:double_exclamation_mark:'))
    print('\nE deverá pagar R$', (velo - 80) * 7, 'reais pela multa.\n')

else:
    print('\nTudo limpo, pode seguir!\n')
    