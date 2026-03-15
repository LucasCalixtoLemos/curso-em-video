# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip()
fraseA = frase.upper()

print(f'Quantas vezes aparece a letra "A": {fraseA.count('A')}')
print(f'Em que posição ela aparece pela primeira vez?: {fraseA.find('A')+1}')
print(f'Em que posição ela aparece pela última vez?: {fraseA.rfind('A')+1}')
