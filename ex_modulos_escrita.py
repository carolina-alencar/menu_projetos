# Exercicio Módulos.
import time
import matplotlib.pyplot as plt


def cont_time():
    valid = False
    repetir = 's'
    print('Escrever seu nome 3 vezes, vamos ver a sua velocidade!')  
    print('Pressione ENTER para começar.')
    input() 
    tempos = []
    
    for i in range (0,3):
        inicio = time.perf_counter()
        input('Escreva seu primeiro nome: ')
        fim = time.perf_counter()
        temp = float(round(fim - inicio,2))
        tempos.append(temp) 
    print(tempos)
    x = [1,2,3]
    legenda = ['1ª vez','2ª vez','3ª vez']
    plt.xticks(x,legenda)
    plt.plot(x,tempos)
    plt.show()
            
 
    #Validação da resposta:
    while valid == False:
        repetir = input('Deseja fazer uma nova tentativa? (s ou n)')
        if repetir != 's' and repetir != 'n':
            print('A resposta deve ser s ou n.')
        elif repetir == 's':
            cont_time()
        else:
            break
            #valid = True

