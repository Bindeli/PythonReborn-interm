# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

# aqui estou empacotando em kwargs
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados: ', args)
    for chave, valor in kwargs.items():
        print(chave,valor)
    print(kwargs)



# mostro_argumentos_nomeados(1,2,3, nome='Joana', qualquer=123)

# posso desempacotar aqui também
# quero desempacotar um dicionário aqui


pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
    'idade'  : 26,
    'altura' : 1.70,
}
# ele vai colocar chave=valor
mostro_argumentos_nomeados(**pessoa)
print('\n\n')
configuracoes = {
    'arg_1' : 1,
    'arg_2' : 2,
    'arg_3' : 3,
    'arg_4' : 4,
    'arg_5' : 5,
}

mostro_argumentos_nomeados(**configuracoes)