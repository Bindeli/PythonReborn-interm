"""
# Sets - Conjuntos em Python (tipo set)

# Conjuntos são ensinados na matemática # https://brasilescola.uol.com.br/matematica/conjunto.htm

# Representados graficamente pelo diagrama de Venn

# Sets em Python são mutáveis, porém aceitam apenas 

# tipos imutáveis como valor interno.


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis; Como lista, dicionários;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

"""
#______________________________________________________________________________________________

# pode ser criado assim : 
# set(iterável) ou {1,2,3}

set_vazio = set()
set_1 = set('Lucas')
# não garante a ordem dos elementos
print(set_1)

# posso criar com o nome completo assim :
print('')
set_2 = {'Lucas', 1 ,2 , 3}
print(set_2)
#______________________________________________________________________________________________
print(f'\nSET remove itens duplicados')
set_3 = {1, 3 , 4 , 3 , 9 , 10 , 9 , 4 , 5, 6}
print(set_3)
lista_4 = [1, 2 , 3 , 3 , 4 , 5 , 6 , 5 , 4 , 10]
print(f'\nLista com itens duplicados : {lista_4}')
set_4= set(lista_4)
print(f'Set : {set_4}')
# Métodos úteis:
# add, update, clear, discard

#______________________________________________________________________________________________
# add para adicionar um valor no set
print('\nUtilizando o ADD no Set')
set_add = set()
set_add.add('Lucas')
set_add.add('2')
set_add.add(3)

print(set_add)
print('\n')
#______________________________________________________________________________________________
# update é muito parecido com add, porém de modar iterada
print('Utilizando o update no set_add: ')
set_add.update('Bindeli')
set_add.update(('Bindeli', 1, 2, 3 , 4 ,5 ))
print(set_add)
print('')
#______________________________________________________________________________________________
# discard eliminar um valor 

set_add.discard('Bindeli')
print(f'SET depois de ter utilizar o discard: {set_add}')
#______________________________________________________________________________________________
# clear para limpar o set
set_add.clear()
print(f'\nSET depois do Clear: {set_add}')

#______________________________________________________________________________________________
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

print(f'\nResumindo tudo: ')

meu_set = {1, 2, 3, 4, 1}
meu_set_2 = set([1, 2, 8, 9, 10])
print(f'Primeiro Set : {meu_set}')
print(f'Segundo Set : {meu_set_2}')

# União
print("União")
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

# Interseção
print("Interseção")
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

# Diferença
print("Diferença")
print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

# Diferença Simétrica
print("Diferença Simétrica")
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))
#______________________________________________________________________________________________
# Exemplo de uso dos sets
# economiza tempo, espaço e rápidos

print('\n')
letras = set()

while True:
    letra = input('Digite : ')
    letras.add(letra)

    #estou buscando a letra l
    if 'l' in letras:
        print(f'parabéns você encontrou a letra misteriosa letra: {letra}')
        break
    print(letras)