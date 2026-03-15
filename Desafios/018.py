# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
ta = math.tan(math.radians(ang))

print(f'Seno     {sen:-^50.2f}')
print(f'Cosseno  {cos:-^50.2f}')
print(f'Tangente {ta:-^50.2f}')
