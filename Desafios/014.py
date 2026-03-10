# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Qual a temperatura em Celsius?: '))
fa = (cel * 9/5) + 32

print(f'{cel} graus Celsius, equivale à {fa} graus Fahrenheit.')
