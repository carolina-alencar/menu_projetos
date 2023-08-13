# Calculo do IMC
def imc(peso, altura):
    valor_imc = peso / (altura*altura)
    return round(valor_imc,1)

# Classificação do IMC

def classific_imc(sexo, peso, altura):
    valor_imc = imc(peso, altura)

    if sexo == 'f':
        if valor_imc < 19.1:
             return 'Mulher abaixo do peso'

        elif valor_imc > 19.1 and valor_imc < 25.8:
             return 'Mulher com peso normal'

        elif valor_imc > 25.8 and valor_imc < 27.3:
             return 'Mulher levemente acima do peso'

        elif valor_imc > 27.3 and valor_imc < 32.3:
             return 'Mulher acima do peso'
        
        else:
             return 'Mulher com obesidade'
    
    else: 
        if valor_imc < 20.7:
             return 'Homem abaixo do peso'

        elif valor_imc > 20.7 and valor_imc < 26.4:
             return 'Homem com peso normal'

        elif valor_imc > 26.4 and valor_imc < 27.8:
             return 'Homem levemente acima do peso'

        elif valor_imc > 27.8 and valor_imc < 31.1:
             return 'Homem acima do peso'

        else:
             return 'Homem com obesidade'

