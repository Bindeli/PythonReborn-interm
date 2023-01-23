# list comprehesion dentro de outro

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))

print(lista)

print('')


lista = []

# lado esquerdo do for, é utilizado para mapeamento
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]

print(lista)