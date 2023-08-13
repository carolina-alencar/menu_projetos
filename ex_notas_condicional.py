#Exercicio:
def media():
    total_aulas = 20
    validar_nota1 = False
    validar_nota2 = False
    validar_falta = False
    continuar = 's'
    valid = False
    nome = input('Digite seu nome completo: ')
    
    # Validar nota 1
    while validar_nota1 == False and continuar == 's':
        nota1 = input('Digite sua primeira nota: ')
        try:
            nota1 = float(nota1)
            if nota1 < 0 or nota1 > 10:
                print('A nota deve ser entre 0 e 10')
            else:
                validar_nota1 = True 
        except:
            print("Valor invalido inserido para nota 1. O valor deve ser numérico, as casas decimais devem ser separadas por '.'")

    # Validar nota 2
    while validar_nota2 == False and continuar == 's':
        nota2 = input('Digite sua segunda nota: ')
        try:
            nota2 = float(nota2)
            if nota2 < 0 or nota2 > 10:
                print('A nota deve ser entre 0 e 10')
            else:
                validar_nota2 = True 
        except:
            print("Valor invalido inserido para nota 2. O valor deve ser numérico, as casas decimais devem ser separadas por '.'")

    # Validar faltas
    while validar_falta == False and continuar == 's':
        faltas = input('Digite o seu total de faltas: ')
        try:
            faltas = int(faltas)
            if faltas < 0 or faltas > 20:
                print("Valor inválido. As faltas são entre 0 e 20")
            else:
                validar_falta = True
        except:
            print('Valor invalido para faltas, dever ser um valor numérico.')

    media_notas = (nota1 + nota2)/2
    assiduidade = ((total_aulas - faltas)/total_aulas)*100
    print(f'Nome: {nome}')
    print(f'Média: {media_notas}')
    print(f'Presença: {assiduidade}%')

    if media_notas >= 6.0:
        if assiduidade >= 70.0:
            print("Aprovado")
    elif media_notas < 6.0:
        if assiduidade >= 70.0:
            print('Reprovado por média')
    elif media_notas >= 6.0:
        if assiduidade < 70.0:
            print('Reprovado por faltas')
    else:
        ("reprovado por faltas e média")
    # Validação da resposta:
    while valid == False:
        continuar = input('Deseja calcular mais uma média? (s ou n): ').lower()       
        if continuar != 's' and continuar != 'n':
            print('A resposta deve ser s ou n.')
        elif continuar == 's':
            media()
        else: 
            valid = True
         
         

