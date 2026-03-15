# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância, em Km, da sua viagem?: '))

if dist <= 200:
    print('Sua passagem vai custar R$', dist * 0.5, 'reais.')

else:
    print('Sua passagem vai curstar R$', dist * 0.45, 'reais.')
    