# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Escreva o nome de uma cidade: ')).strip()
truefalse = cidade.upper()[:5] == 'SANTO'

print(f'A cidade que você escolheu começa com "Santo"?: {truefalse} ')
