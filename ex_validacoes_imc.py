import ex_imc_funcao as func # Dessa forma importa todas as funções do módulo
  
#from ex_imc_funcao import imc, classific_imc (Dessa forma voce defini quais funções quer importar, dessa maneira não precisa informar a qual módulo pertence a função)

def calcular_imc():
    print('Vamos calcular seu IMC?')
    repetir = 's'
    valid_peso = False
    valid_altura = False
    valid_sexo = False
    valid_sn = False

    # Validação do peso
    while valid_peso == False and repetir == 's':
        peso =(input('Digite seu peso: '))
        try:
            peso = float(peso)
            if peso <= 0: # Para o valor não ser negativo
                print('O peso precisa ser maior que zero')
            else:
                    valid_peso = True
        except:
            print("formato de peso invalido. Use apenas numeros, separe as casas decimais com '.'' ")
            
    # Validação da altura
    while valid_altura == False and repetir == 's':
        altura =(input('Digite sua altura: '))
        try:
            altura = float(altura)
            if altura <= 0: # Para o valor não ser negativo
                print('A altura precisa ser maior que zero')
            else:
                    valid_altura = True
        except:
            print("formato da altura é invalido. Use apenas numeros, separe as casas decimais com '.'' ")

    # Validação do sexo
    while valid_sexo == False and repetir == 's':
        sexo = input('Digite seu sexo (M ou F): ').lower().strip()
        if sexo != 'm' and sexo != 'f':
            print('O Sexo deve ser M ou F')
        else:
            valid_sexo = True

    v_imc = func.imc(peso, altura) 
    c_imc = func.classific_imc(sexo, peso, altura) 

    print(f'O seu imc é {v_imc}')
    print(f'A sua clasificação imc é: {c_imc}')

    #Validar a resposta se deseja sair ou continuar 
    while valid_sn == False:
        repetir = input('Deseja calcular mais um IMC? (s ou n)').lower()       
        if repetir != 's' and repetir != 'n':
            print('A resposta deve ser s ou n.')      
        elif repetir == 's':
            calcular_imc()
        else: 
         valid_sn = True
    
        