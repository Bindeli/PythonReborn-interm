# Manipulando chaves e valores em dicionarios

pessoa = {} # dicionário vazio

# criando uma chave com valor
pessoa['nome'] = 'Lucas'

print(pessoa['nome'])
print(pessoa)
print('')
#______________________________________________________________________________________________
# Chaves dinâmicas

var_sobrenome = 'sobrenome'
pessoa[var_sobrenome] = 'Bindeli'
print(pessoa[var_sobrenome])
print(pessoa)
print('')

var_idade = 'idade'
pessoa[var_idade] = 25
print(pessoa[var_idade])
print(pessoa)
#______________________________________________________________________________________________
# Apagar uma chave utilizando del
print('\nDepois de apagar a chave idade com a função del')
del pessoa[var_idade]
print(pessoa)

print('\n')
#______________________________________________________________________________________________
"""
Se eu chamar a chave idade agora, vai dar um erro chamado KeyError

Posso usar um método get que impede erro e verifica se existe ou não

Por padrão ele retorna None se a chave não existe, mas posso colocar o que deve aparecer
depois da vírgula

Se a chave existe, ele retorna a chave
"""

# print(pessoa.get('idade', 'Não existe'))

if pessoa.get('idade') is None:
    print('Não existe')
else:
    print(pessoa['idade'])







