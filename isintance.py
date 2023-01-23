# isinstace - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 2, 2.2, True, [0,1,2], (1,2), {0,1}, {'nome':'Lucas'}
]


for item in lista:
    if isinstance(item,set):
        print(item, isinstance(item, set), 'é um set!')

    if isinstance(item, str):
        print(item, isinstance(item, str), 'é uma string')

    if isinstance(item, (int, float)):
        print(item, isinstance(item, (int, float)), 'é um número')