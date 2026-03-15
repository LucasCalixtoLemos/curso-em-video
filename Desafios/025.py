# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual o seu nome?: '))

print(f'Tem Silva no seu nome?: {'silva' in nome.lower()}')
