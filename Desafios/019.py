# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1 = str(input('Qual o nome do 1º aluno?: '))
a2 = str(input('Qual o nome do 2º aluno?: '))
a3 = str(input('Qual o nome do 3º aluno?: '))
a4 = str(input('Qual o nome do 4º aluno?: '))

lista = [a1, a2, a3, a4]

escolha = random.choice(lista)

print(f'O aluno escolhido foi {escolha}.')
