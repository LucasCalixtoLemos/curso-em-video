# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = str(input('Qual o nome do 1º aluno?: '))
a2 = str(input('Qual o nome do 2º aluno?: '))
a3 = str(input('Qual o nome do 3º aluno?: '))
a4 = str(input('Qual o nome do 4º aluno?: '))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print(f'A ordem é: {lista}')
