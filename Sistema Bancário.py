menu = '''
        MENU
        [D]-Depositar
        [S]-Sacar
        [E]-Extrato
        [Q]-Sair
'''
saldo = float(0.0)
limite = float(500.0)
n_saques = int(0)
lim_saque = 3
extrato = ''
while True:
    opt = input(menu).upper()
    if opt == 'D':
        deposito = float(input('Digite o valor do depósito: '))
        saldo += deposito
        extrato = extrato + f'Depósito de: R${saldo:.2f}\n'
    elif opt == 'S':
        saque = float(input('Digite o valor do saque: '))
        if saque > 0:
            if n_saques < lim_saque:
                if saque > limite:
                    print('Valor indisponível\nPermitido somente R$500,00 por saque.')
                else:
                    if saldo >= saque:
                        saldo -= saque
                        n_saques += 1
                        print('Retire o valor na boca do caixa!')
                        extrato = extrato + f'Saque de: R${saque:.2f}\n'
                    else:
                        print('Saldo insuficiente para saque!')
            else:
                print('Limite de 3 saques excedido!\nOperação cancelada.')
        else:
            print('Não é possível sacar esta quantia!')
    elif opt == 'E':
        if extrato == '':
            print('Não foram realizadas movimentações.')
        else:
            print(extrato)
    elif opt == 'Q':
        break
    else:
        print('Opção inválida!')
