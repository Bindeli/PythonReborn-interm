"""
Introdução à função lambda (função anônima de uma linha)

A função lambda é uma função como qualquer outra em python.
Porém, são funções anônimas que contém apenas uma linha.

Ou seja, tudo deve ser contido dentro de uma única expressão
"""

#______________________________________________________________________________________________
# Método sort para ordernar minha lista

lista_desordenada = [1,7,9,2,3,5,4,6,8]
print(f'\nLista desordenada: {lista_desordenada}')
lista_desordenada.sort()
print(f'Utilizando o método sort : {lista_desordenada}')
lista_desordenada.sort(reverse=True)
print(f'Utilizando sort com reverse true:  {lista_desordenada}')

#______________________________________________________________________________________________

lista_dicion = [
    {'nome' : 'Lucas' , 'Sobrenome' : 'Bindeli'},
    {'nome' : 'Nil', 'Sobrenome': 'Ribeiro'},
    {'nome' : 'André', 'Sobrenome': 'Júnior'},
    {'nome' : 'Marcelo', 'Sobrenome' : 'Lemão'},
    {'nome' : 'Dalva', 'Sobrenome': 'Camara'},
]

# o python não vai saber ordernar apenas passando o sort
# porém posso passar uma função para o sort

def orderna(item):
    return item['nome']


lista_dicion.sort(key=orderna)
print(f'Lista ordernada:')
for item in lista_dicion:
    print(item)

#______________________________________________________________________________________________

# posso fazer isso com a função lambda
# lambda seria def

lista_dicion.sort(key= lambda item: item['nome'])

print('\nLista ordenada com a função lambda: ')

for item in lista_dicion:
    print(item)
#______________________________________________________________________________________________
print('')

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista_dicion, key=lambda item: item['nome'])
l2 = sorted(lista_dicion, key=lambda item: item['Sobrenome'])

print('Lista com sorted, ordernada pelo nome')
exibir(l1)
print('Lista com sorted, ordernada pelo sobrenome')
exibir(l2)

print('\n\n')