# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

titulo = 'BANCO DO BRASIL'

print('')
print('-=-'*20)
print(f'{titulo:^60}')
print('-=-'*20)

preco = float(input('\nQUAL O PREÇO DO PRODUTO?: '))
print('\n- ESCOLHA O TIPO DE PAGAMENTO')
print('1. Á VISTA EM DINHEIRO OU CHEQUE\n2. À VISTA NO CARTÃO\n3. EM ATÉ 2 VEZES NO CARTÃO\n4. 3X OU MAIS NO CARTÃO')
avistaouparc = int(input('ESCOLHA: '))

if avistaouparc == 1:
    print(f'\nVOCÊ PAGARÁ R${preco * 0.9:.2f}\n')

elif avistaouparc == 2:
    print(f'\nVOCÊ PAGARÁ R${preco * 0.95:.2f}\n')

elif avistaouparc == 3:
    print(f'\nVOCÊ PAGARÁ R${preco:.2f}\n')

elif avistaouparc == 4:
    qntdparc = int(input('QUANTAS VEZES VOCÊ QUER PARCELAR?: '))
    print(f'PARCELANDO {qntdparc} VEZES, VOCÊ PAGARÁ R${(preco / qntdparc)*1.2} HOJE.')

else:
    print('\nESCOLHA INVÁLIDA\n')
