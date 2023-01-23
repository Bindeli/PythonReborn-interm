"""
Dicionários em python - dict()

São estruturas de dados do tipo par de chave e valor, coisas que podem ter atributos

Chaves podem ser consideradas como o indice que vimos nas listas e podem ser tipos imutáveis
Como : STR, INT, FLOAT, BOOL, TUPLE. ETC

O valor pode ser qualquer tipo, incluindo outro dicionário.

Usamos as chaves {} ou a classe dict para criar dicionários

Imutáveis : str, int, float, bool, tuple
Mutáveis: dict, list

pessoa: {
    'nome' : 'Lucas',
    'sobrenome' : 'Bindeli',    
    'idade' : 25,
    'altura' : 1.70,
    'endereços' : [
        {'rua':'São joão', 'numero': 68},
        {'rua' : 'tal tal', 'numero': 101},
    ]
}
"""

pessoa = {
    'nome': 'Lucas',
    'sobrenome' : 'Bindeli',
    'idade': 25,
}
#______________________________________________________________________________________________
# para acessar a chave do dicionário:
print('\nPrintando apenas as chaves')
for chave in pessoa:
    print(chave)
print('\n')
#______________________________________________________________________________________________
# para acessar as chaves e o valor colocamos o dicionario[chave]
print('Acessando os valores')
for chave in pessoa:
    print(f'Chave: {chave} e valor : {pessoa[chave]}')

print('\n')
#______________________________________________________________________________________________
# items para acessar os dois
for chave, valor in pessoa.items():
    print(f'Chave : {chave} e valor: {valor}')

#______________________________________________________________________________________________