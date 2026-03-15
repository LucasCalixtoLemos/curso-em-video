# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Qual o tamanho do lado A?: '))
b = float(input('Qual o tamanho do lado B?: '))
c = float(input('Qual o tamanho do lado C?: '))

if a + b > c and a + c > b and b + c > a:
    print('Elas formam um triângulo!')

else:
    print('Elas não formam um triângulo...')
