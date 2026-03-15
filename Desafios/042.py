# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

from time import sleep

titulo = 'O ANALISTA DE TRIÂNGULOS' 

print('-^-' * 20)
print(f'\033[1;31m{titulo:^60}\033[m')
print('-^-'*20)

a = float(input('\n\033[1;32mQUAL O TAMANHO DO PRIMEIRO LADO?: \033[m '))
b = float(input('\n\033[1;32mQUAL O TAMANHO DO SEGUNDO LADO?: \033[m '))
c = float(input('\n\033[1;32mQUAL O TAMANHO DO TERCEIRO LADO?: \033[m '))
truetri = a + b > c and a + c > b and b + c > a

print('\n\033[4;36mPROCESSANDO...\033[m\n')
sleep(1.5)

if truetri and a == b and b == c:
    print('ESSES LADOS FORMARÃO UM TRIÂNGULO \033[1;32mEQUILÁTERO!\n')

elif truetri and a == b or a == c or b == c:
    print('ESSES LADOS FORMARÃO UM TRIÂNGULO \033[1;32mISÓSCELES!\n')

elif truetri and a != b and a != c and b != c:
    print('ESSES LADOS FORMARÃO UM TRIÂNGULO \033[1;32mESCALENO!\n')

else:
    print('ESSES LADOS NÃO FORMARÃO UM \033[1;31mTRIÂNGULO!\033[m\n')
