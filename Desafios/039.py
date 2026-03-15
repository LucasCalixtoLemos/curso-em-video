# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

titulo = 'JUNTA MILITAR'
print('[]'*30)
print(f'\033[1;35m{titulo:^60}\033[m')
print('[]'*30)

atual = date.today().year
nascimento = int(input('\nEM QUE ANO VOCÊ NASCEU?: \033[1;32m\033[m'))
idade = atual - nascimento

print(f'\n\033[1mVOCÊ TEM {idade} NOS DE IDADE.\033[m\n')

if idade < 18:
    print(f'DAQUI A {18 - idade} ANO(S) VOCÊ DEVERÁ SE ALISTAR! EM {(18 - idade) + 2026}.\n')

elif idade == 18:
    print('É HORA DE SE ALISTAR\n')

else:
    print(f'VOCÊ JÁ PASSOU {idade - 18} ANO(S) DA IDADE DE ALISTAMENTO.\n')
