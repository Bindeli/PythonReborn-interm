# Empacotamento e desempacotamento de dicionários

a,b = 1,2 
a,b = b,a
print(a,b)
print('\n')
#___________________________________________________________________________________________________

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
}

#desempacotar internamente
# (a1, a2), b = pessoa.items()

# print(a1,a2, b) # nome Aline ('sobrenome', 'Souza')

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade'  : 26,
    'altura' : 1.70,
    
}

# como eu fazia para juntar esses dois dicionários ?

# posso criar um terceiro dicionário e jogar a extreção desses valores

# * somente um para extrair a chave, ** dois para trazer a chave e o valor
#desempacotamento
pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

#___________________________________________________________________________________________________













#___________________________________________________________________________________________________
