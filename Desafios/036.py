# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual é o seu salário?: '))
anos = int(input('Por quantos anos você vai pagar?: '))
prestacao = valor / anos * 12
limite = 0.3 * salario

if prestacao <= limite:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')
    