# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quantos reais você tem na carteira?: '))
qtd_dolares = real / 5.21

print(f'Com {real:.2f} reais, você pode comprar {qtd_dolares:.2f} dólares!')
