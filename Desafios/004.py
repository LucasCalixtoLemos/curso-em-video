# Crie um programa que identifique o tipo primitivo de um valor digitado pelo usuário e mostre na tela todas as informações possíveis sobre ele.
n = input('Digite algo: ')

print('O tipo primitivo da sua escolha é', type)

print('A sua escolha só tem espaços?', n.isspace())
print('A sua escolha é um número?', n.isnumeric())
print('A sua escolha faz parte do alfabeto?', n.isalpha())
print('A sua escolha está em maiúsculo?', n.isupper())
print('A sua escolha está em minúsculo?', n.islower())
print('A sua escolha está capitalizada?', n.istitle())



