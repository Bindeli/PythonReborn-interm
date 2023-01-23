# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)

# list comprehension eu faço assim :

lista = [numero for numero in range(10)]
lista_dobro = [numero * 2 for numero in range(10)]
# posso pegar o for e pegar a variavel do for normal, passar um iteravel, e do iteravel pegar a variavel
# e colocar a esquerda do for que ele vai incluir isso na lista
# print(lista)
# print(lista_dobro)
#______________________________________________________________________________________________
# mapeamento de dados em list comprehension
# pegando dados de um iteravel, transformando os dados colocando na outra lista
# os dois devem ter o mesmo tamanho

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 15, },
]

# novos_produtos = [produto['nome'] for produto in produtos]

# uma lista que só tem os nomes
# novos_produtos = [produto['nome'] for produto in produtos]

# print(*novos_produtos, sep='\n')
#______________________________________________________________________________________________
# para criar um novo dicionário eu faço assim :

# novos_produtos = [{} for produto in produtos] # assim ele estará vazio
novos_produtos = [{'nome': produto['nome'],'preco':produto} for produto in produtos]
print(novos_produtos)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    for produto in produtos ]

print(f'Alterando o preço : {novos_produtos}')

#caso eu queira aumentar o valor do produtor somente se o valor for maior ou igual a 20 reais

novos_produtos = [ {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] >= 20 else {**produto} for produto in produtos ]


print(f'\n20 acima : {novos_produtos}')

"""
[!]
O que vêm a esquerda do for é mapeamento
o que vêm a direita é filtro

"""


#______________________________________________________________________________________________
# filter

# incluir determinadas coisas que você quer que apareça

# o if irá depois do for e não tem else

lista_nova = [numero for numero in range(10) if numero < 5]
print('')
print(lista_nova)

produtos_2 = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 15, },
    {'nome': 'p5', 'preco': 50, },
]

novos_produtos = [ {**produto, 'preco' : produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos_2 
    if produto['preco'] > 15 # esse pega o valor antigo e ignora o aumento de cima
    # caso eu queira incluir com aumento seria assim : 
    # if produto['preco'] * 1.05 > 15
]
print('\n')    
print(novos_produtos)



#______________________________________________________________________________________________
# deixar o print de dicionário mais bonito

# import pprint

# def printando(valor):
#     pprint.pprint(valor, sort_dicts=False, width=40)

print('\n\n')