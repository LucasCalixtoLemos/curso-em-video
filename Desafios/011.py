# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura, em metros, da parede?: '))
altura = float(input('Qual a altura, em metros, da parede?: '))

area = largura * altura
litros = area / 2

print(f'A parede mede {area} metros quadrados, sendo assim, serão necessários {litros} litros de tinta para pintá-la.')
