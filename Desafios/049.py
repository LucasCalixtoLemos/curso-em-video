#  Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('DIGITE UM NÚMERO: '))
cont = 0

for cont in range(1, 11):
    tabuada = cont * num
    print(f'{num} X {cont} = {tabuada}')