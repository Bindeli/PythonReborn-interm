# Exercícios com funções
#___________________________________________________________________________________________________

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for valor in args:
        total *= valor
        
    return total

conjunto_numeros = 1,2,3,4,5,6,7,8,9
resultado_1 = multiplica(1,2,3,4,5)
resultado_2 = multiplica(*conjunto_numeros)
print(f'Resultado 1 : {resultado_1}')
print(f'Resultado 2 : {resultado_2}\n')

#___________________________________________________________________________________________________

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
print('\nExercicio 2:')

def par_impar(*args):
    for elemento in args:
        if elemento % 2 ==0 :
            print(f'O elemento {elemento} é par')
        else:
            print(f'O elemento {elemento} é ímpar')
    
par_impar(2)
conj_numeros_2 = 2,4,6,21,3,17,8,9
par_impar(*conj_numeros_2)
"""
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    """