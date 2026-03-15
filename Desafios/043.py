# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

titulo = 'CALCULADORA DE IMC'

print('-<-' * 20)
print(f'{titulo:^60}')
print('->-' * 20)

peso = float(input('\nQUAL É O SEU PESO EM KG?: '))
altura = float(input('\nQUAL É A SUA ALTURA EM METROS?:'))
imc = peso / altura**2

if imc < 18.5:
    print(f'\nSEU IMC É {imc:.2f} E VOCÊ ESTÁ ABAIXO DO PESO!\n')

elif imc >= 18.5 and imc < 25:
    print(f'\nSEU IMC É {imc:.2f} E VOCÊ ESTÁ NO PESO IDEAL!\n')

elif imc >= 25 and imc < 30:
    print(f'\nSEU IMC É {imc:.2f} E VOCÊ TEM SOBREPESO!\n')

elif imc >= 30 and imc < 40:
    print(f'\nSEU IMC É {imc:.2f} E VOCÊ TEM OBESIDADE!\n')

else:
    print(f'\nSEU IMC É {imc:.2f} E VOCÊ TEM OBESIDADE MÓRBIDA!\n')
