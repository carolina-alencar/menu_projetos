# Menu de exercicios
import ex_validacoes_imc as imc
import ex_loop_fatura as fat
import ex_notas_condicional as notas
import ex_modulos_escrita as digitar

lista_ex = [1,2,3,4,5]
# Validação da resposta:
repetir = 's'
valid_resposta = False
while valid_resposta == False and repetir == 's':

    print('------------------------------MENU EXERCÍCIOS-----------------------------------')
    print('1- CALCULO DE IMC --------------------------------------------------------------')
    print('2- FATURA DE COMPRAS -----------------------------------------------------------')
    print('3- VELOCIDADE DE DIGITAÇÃO -----------------------------------------------------')
    print('4- CALCULO DE MÉDIA DE NOTAS ---------------------------------------------------')
    print('5- SAIR ------------------------------------------------------------------------')

    resposta = (input('ESCOLHA O NÚMERO CORRESPONDENTE AO PROGRAMA DESEJADO PARA EXECUTA-LO: '))
    try: 
        resposta = int(resposta) 
        if resposta not in lista_ex: 
            print(f'O NÚMERO DEVE EXISTIR NO MENU (ENTRE 1 E {lista_ex[-1]})')   
    except: 
        print("formato invalido. Use apenas numeros.")

    if repetir == 's':
        if resposta == 1:
            imc.calcular_imc()     
        elif resposta == 2: 
            fat.faturas()
        elif resposta == 3: 
            digitar.cont_time()          
        elif resposta == 4: 
            notas.media() 
        elif resposta == 5:
            print('Saindo do Menu')
            repetir = 'n'
            valid_resposta = True



