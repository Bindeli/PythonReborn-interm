produto = {
    'nome' : 'caderno',
    'preco' : 20,
    'categoria' : 'escritorio',
}

dict_c = {
    chave : valor.upper()
    if isinstance(valor, str) else valor # para checar se valor é uma string
    # chave : valor
    # if isinstance(valor, (int, float)) else valor.upper() # ao contrário seria assim
    for chave, valor in produto.items()
    # if chave != 'categoria'    para excluir a coluna
}

print(dict_c)
print('\n')

lista = [
    ('a', 'valor_a'),
    ('b', 'valor_b'),
    ('c', 'valor_c'),
    ('d', 'valor_d'),
]

dict_list = {
    chave : valor 
    for chave, valor in lista
}

# ou simplesmente dict(lista)

print(dict_list)








