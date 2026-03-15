# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome completo?: '))

print(f'Seu nome em letras maiúsculas: {nome.upper()}')
print(f'Seu nome em letras minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome)}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')
