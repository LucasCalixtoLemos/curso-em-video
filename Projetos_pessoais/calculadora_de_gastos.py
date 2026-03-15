# TÍTULO
titulo = 'CALCULADORA DE GASTOS'
print('\n'+'\033[1;35m-=-\033[m' * 39)
print(f'\033[1;37m{titulo:-^117}')
print('\033[1;35m-=-\033[m' * 39)

# INPUTS INICIAIS
saldo_inicial = float(input('\n\033[1;34mQUAL É O SEU SALDO INICIAL?: \033[1;32m'))
gasto_diario = float(input('\n\033[1;34mQUANTO VOCÊ GASTOU HOJE?: \033[1;31m'))

# SAÍDAS
titulo_saidas = 'ANÁLISES'
print('\n'+'\033[1;35m-=-\033[m' * 39)
print(f'\033[1;37m{titulo_saidas:-^117}\n')

print(f'\033[1;32mSALDO INICIAL:\033[m R${saldo_inicial}')
print(f'\n\033[1;34mSALDO FINAL:\033[m R${saldo_inicial - gasto_diario}')
print(f'\n- {(gasto_diario / saldo_inicial) * 100}% DO SEU DINHEIRO FOI GASTO \033[1;31mHOJE\033[m\n')

if (gasto_diario / saldo_inicial) * 100 <= 30:
    print('\033[1;32mEXCLENTE\033[m CONTROLE!\n')

elif (gasto_diario / saldo_inicial) * 100 > 30 and (gasto_diario / saldo_inicial) * 100 <= 50:
    print('CONTROLE \033[1;36mRAZOÁVEL.\033[m\n')

elif (gasto_diario / saldo_inicial) * 100 > 50 and (gasto_diario / saldo_inicial) * 100 <= 80:
    print('\033[1;34mCUIDADO\033[m COM OS GASTOS!\n')

else:
    print('\033[1;31mSITUAÇÃO CRÍTICA!\033[m\n')
