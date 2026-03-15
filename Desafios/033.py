# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha outro número: '))
n3 = float(input('Escolha outro número: '))

# n1 MAIOR NÚMERO
if n1 > n2 and n2 > n3:
    print('Maior número:', n1)
    print('Menor número:', n3)

elif n1 > n3 and n3 > n2:
    print('Maior número:', n1)
    print('Menor número:', n2)

# n2 MAIOR NÚMERO
elif n2 > n1 and n1 > n3:
    print('Maior número:', n2)
    print('Menor número:', n3)

elif n2 > n3 and n3 > n1:
    print('Maior número:', n2)
    print('Menor número:', n1)

# n3 MAIOR NÚMERO
elif n3 > n2 and n2 > n1:
    print('Maior número:', n3)
    print('Menor número:', n1)

else:
    print('Maior número:', n3)
    print('Menor número:', n2)
