#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
#titulo
titulo = 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO'
print('->-'*20)
print(f'\033[4;33m{titulo:^60}\033[m')
print('-<-'*20)


atual = date.today().year
ano_nascimento = int(input('\nEM QUE ANO VOCÊ NASCEU?: '))
idade = atual - ano_nascimento

if idade <= 9:
    print(f'\nVOCÊ TEM \033[1;32m{idade}\033[m ANOS DE IDADE, E FAZ PARTE DA CATEGORIA \033[1;32mMIRIM!\033[m.\n')

elif idade > 9 and idade <= 14:
    print(f'\nVOCÊ TEM \033[1;32m{idade}\033[m ANOS DE IDADE, E FAZ PARTE DA CATEGORIA \033[1;32mINFANTIL!\033[m.\n')

elif idade > 14 and idade <= 19:
    print(f'\nVOCÊ TEM \033[1;32m{idade}\033[m ANOS DE IDADE, E FAZ PARTE DA CATEGORIA \033[1;32mJÚNIOR!\033[m.\n') 

elif idade > 19 and idade <= 25:
    print(f'\nVOCÊ TEM \033[1;32m{idade}\033[m ANOS DE IDADE, E FAZ PARTE DA CATEGORIA \033[1;32mSÊNIOR!\033[m.\n')

else:
    print(f'\nVOCÊ TEM \033[1;32m{idade}\033[m ANOS DE IDADE, E FAZ PARTE DA CATEGORIA \033[1;32mMASTER!\033[m.\n')
