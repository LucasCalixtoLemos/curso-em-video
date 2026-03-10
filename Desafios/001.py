# Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nome = input('Qual o seu nome?: ')
#print('Olá', nome, '! Prazer em te conhecer!')
print('Olá {}! Prazer em te conhecer!'.format(nome))
