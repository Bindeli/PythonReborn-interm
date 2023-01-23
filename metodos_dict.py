"""
# Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro

"""
pessoa = {
    'nome' : 'Lucas',
    'sobrenome': 'Bindeli',
    'idade' : 25,
}

print('\n')
#______________________________________________________________________________________________
# len não é um método que está diretamente ligada ao dicionário
# retorna a quantidade de chaves que eu tenho no dicionário

print(f'Vendo quantas chaves possui com len: {len(pessoa)}\n')


#______________________________________________________________________________________________
"""
pessoa = {
    'nome' : 'Lucas',
    'sobrenome': 'Bindeli',
    'idade' : 25,
    'idade' : 26
}

Se eu der nomes iguais para a chave, o valor final será o último, como se fosse uma atualização

Ainda será contado como 3 chaves.
"""
#______________________________________________________________________________________________
# com o KEYS, posso iterar com as chaves, ele retorna um dict_keys com o valores

print(pessoa.keys())

# e convertindo ele, exemplo para uma tupla, podemos iterar

pessoa_tupla = tuple(pessoa.keys())
print('Iterando depois de converter')
for item in pessoa_tupla:
    print(item)
print(f'\nVerificando no indice 2: {pessoa_tupla[2]}')
#______________________________________________________________________________________________
# com o VALUES, posso iterar com os valores das chaves
print('\nIterando com o VALUES')
print(list(pessoa.values()))
print('Iterando com o for utilizando o values: ')
for valores in pessoa.values():
    print(valores)
print('')
#______________________________________________________________________________________________
# com o items, posso ter acesso tanto as chaves como seus valores
print('Utilizando items para acessar chaves e valores')
for chave, values in pessoa.items():
    print(f'Chave: {chave} - Valor: {values}')
print('')
#______________________________________________________________________________________________
"""
setdefault - adicionar valor se a chave não existe
"""
print('Utilizando o setdefault')
pessoa.setdefault('altura', 0) # já que não existe, vai adicionar
# se existisse, iria retornar o valor que está no dicionário.
print(pessoa)
print('')
#______________________________________________________________________________________________
"""
Shallow Copy - cópia rasa, 

Deep Copy -

d2 = d1 - vai copiar porém ambos estão apontando para o mesmo objeto com o mesmo endereço 
na memória

"""
d1 = {
    'c1': 1,
    'c2': 2,
}

# se eu fizer isso, d2 = d1, qualquer alteração feita em d2, vai passar para d1

d2 = d1.copy() # d2 vai receber uma cópia do d1, posso alterar os valores de d2, sem mexer no d1

d2['c1'] = 1000
print(f'Dicionário d1: {d1}')
print(f'Dicionário d2 : {d2}')

# copia rasa é tudo que for uma cópia rasa, ele vai copiar para o outro dicionário
# se eu tiver valores mutáveis, como uma lista, os dois dicionários terão a lista 
# apontando para o endereço da mesma lista

d_list = {
    'c1' : 1,
    'c2' : 2,
    'lista' : [1,2,3,4,5],

}

d3 = d_list.copy()

print(d3)
# se eu mudar um valor na lista do d3, o d_list irá sofrer mudança também
d3['lista'][2] = 100
print(f'D_LIST = {d_list}')
print(f'D3 = {d3}')
# ambos os dicionários apontam para a mesma lista

"""
Caso eu queira fazer uma copia total, eu preciso puxar da biblioteca copy, um módulo.

deep_d2 = copy.deepcopy(deep_d1)

"""
import copy

# posso puxar do copy também para fazer uma copia rasa # d3 = copy.copy(d_list)

deep_d1 = {
    'estado': 'ES',
    'cidade' : 'Cariacica',
    'endereco' : ['Rua são João','Bairro Santo André', '68'],
}
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
deep_d2 = copy.deepcopy(deep_d1)

# agora sim, é uma cópia total, posso alterar os valores

print('\nDicionarios deep: ')
print(f'Dicionário deep 1 : {deep_d1}')
print(f'Dicionário deep 2 : {deep_d2}')
print('Mudando os valores da tabela do deep 2: ')
deep_d2['endereco'][2] = 'valor alterado'
print(f'Dicionário deep 1 : {deep_d1}')
print(f'Dicionário deep 2 após mudança : {deep_d2}')

print('')
#______________________________________________________________________________________________
# get - obtém uma chave do dicionário, e retorna ou None (se não tiver) ou o valor 
print('GET')
p1 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Fernandes',
    'cargo' : 'funcionário público',
}

print(p1.get('nome'))
print(p1.get('idade', 'Não existe'))
print('')

#______________________________________________________________________________________________
# pop - Apaga um item com a chave especificada

# quero Apagar o valor de cargo, e quero também obter o valor, posso fazer isso
print(p1)
cargo = p1.pop('cargo')
print(f'Foi apagado este : {cargo}')
print(f'Situação atual do dicionário P1: {p1}')
#______________________________________________________________________________________________
# popitem - Apaga o último item adicionado
print('')
print(p1)
ultimo_apagado = p1.popitem()
print(f'O último apagado será : {ultimo_apagado}')
print(f'Situação atual depois do popitem : {p1}')
#______________________________________________________________________________________________
# update - Atualiza um dicionário com outro, dicionario.update( {} )
# ele não altera as chaves não-mencionadas
# e posso adicionar novas chaves e valores

p2 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Fernandes',
    'cargo' : 'funcionário público',
}

print('\nUpdate - atualizando informações!')
print(f'Dicionário P2 neste momento : {p2}')
p2.update({
    'nome' : 'Novo Nome',
    'sobrenome' : 'Bindeli',
    'idade' : '25'
})

print(f'Dicionário P2 após update: {p2}')
print(f'Utilizando o update de outra forma, com argumentos nomeados:')

# criando chaves com os argumentos nomeados também
p2.update(nome='Lucas', idade='26')
print(f'Dicionário P2 depois de outra modificação: {p2}')

# tupla = ('nome','lucas'), ('idade', 25)
# p1.update(tupla)
# faria a mesma coisa, consigo com lista também
#______________________________________________________________________________________________




print('\n\n')