# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

co = float(input('Qual o cateto oposto do triângulo?: '))
ca = float(input('Qual o cateto adjacente do triângulo?: '))
hip = math.hypot(co, ca)

print(f'A hipotenusa do triângulo é {hip}.')
