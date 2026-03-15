# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

titulo = 'CONVERSOR'

print("\033[1;35m-=-\033[m" * 20)
print(f'\033[1m{titulo:^60}')
print("\033[1;35m-=-\033[m" * 20)

num = int(input('\n\033[1;32mNÚMERO PARA CONVERTER: \033[m'))

print('CONVERTER PARA:')
print('\n[1]\033[1;32m BINÁRIO\033[m')
print('[2]\033[1;32m OCTAL\033[m')
print('[3]\033[1;32m HEXADECIMAL\033[m')

escolha = int(input('\nSELECIONE SUA OPÇÃO: '))

if escolha == 1:
    print(f'\n{num} EM NÚMERO BINÁRIO É {bin(num)[2:]}.\n')

elif escolha == 2:
    print(f'\n{num} EM NÚMERO OCTAL É {oct(num)[2:]}.\n')

elif escolha == 3:
    print(f'\n{num} EM NÚMERO HEXADECIMAL É {hex(num)[2:]}.\n')

else:
    print('\n\033[1;31mESCOLHA UMA OPÇÃO EXISTENTE!\033[m\n')