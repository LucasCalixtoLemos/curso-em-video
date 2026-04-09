# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for cont in range(1,7):
    n = int(input('DIGITE UM NÚMERO: '))
    if n % 2 == 0:
        soma += n
print(soma)

