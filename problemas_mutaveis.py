# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista
    

# aqui eu não passo a lista, pois a lista está sendo criada agora
cliente_1 = adiciona_clientes('Lucas')

# aqui eu preciso passar a lista, pois ela já existe, passo o nome e a lista
adiciona_clientes('Joana', cliente_1)
print(cliente_1)

"""
Porém isso gera um bug, toda a vez que eu passar essa função
mesmo com uma outra variável, o python vai puxar a mesma lista

qualquer parâmetro mutável vai dar este problema
"""
cliente_2 = adiciona_clientes('Maria')
adiciona_clientes('Helena', cliente_2) # ['Lucas', 'Joana', 'Maria', 'Helena']
print(cliente_2)

#_____________________________________________________________________________________________

# então como resolver esse problema e ter uma lista nova todas as vezes ?
# uma maneira de resolver isso é ter uma lista fora da função e chamar na primeira vez
print('\n\n')
lista_1 = []
cliente_1 = adiciona_clientes('Lucas', lista_1)
adiciona_clientes('Joana', cliente_1)
print(cliente_1)

lista_2 = []
cliente_2 = adiciona_clientes('Maria', lista_2)
adiciona_clientes('Helena', cliente_2) 
print(cliente_2)
print('\n')
#_____________________________________________________________________________________________
# O ideal seria não utilizar parâmetros mutáveis como parâmetros na função

# posso passar um parâmetro imutável

print('\nDepois de ter utilizado o parâmetro como None:')
def adicionar(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

# e toda as vezes que eu for chamar igual fiz anteriormente, terei uma lista nova

cliente_1 = adicionar('Lucas')
adicionar('Joana', cliente_1)
cliente_1.append('Eduardo')
print(cliente_1)

cliente_2 = adicionar('Maria')
adicionar('Helena', cliente_2) 
print(cliente_2)
print('\n')
#_____________________________________________________________________________________________
"""
Toda vez que eu criar um parâmetro na função em Python, tenho que checar se ele é mutável

Se ele for mutável, não colocar valor padrão

um exemplo, utilizar o None, se ninguém enviar, você cria o parâmetro igual o exemplo de if
"""

print('\n\n')