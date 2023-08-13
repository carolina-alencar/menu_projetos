#exercicio com loop

def faturas():
    repetir = 's'
    continuar =                           's'
    fatura = []
    total = 0
    valid = False
    while repetir == 's' and continuar == 's':
        produto = input('Digite o nome do produto: ')
        preco = float(input('Digite o valor do produto: '))
        fatura.append([produto,preco])
        total += preco
        repetir = input('Deseja mais um produto? (s ou n)').lower()

    #imprimir produtos e os preços
    for i in fatura:
        print(i[0],'-',i[1])

    print(f'total: {total}')

     #Validar a resposta se deseja sair ou continuar 
    while valid == False:
        continuar = input('Deseja continuar no programa? (s ou n)').lower()       
        if continuar != 's' and continuar != 'n':
            print('A resposta deve ser s ou n.')
        elif continuar == 's':
            faturas()
        else: 
            valid = True