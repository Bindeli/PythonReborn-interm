"""
Checar quais coisas estão dentro do objeto

dir - vai me mostrar todos os métodos definidos do objeto
hasattr - 
"""

# quais métodos estão disponíveis dentro da minha string ? 

# dir vai me mostrar todos os métodos definidos do objeto, no caso a string

string = 'Lucas'

# hasattr checa se determinado objeto possui um determinado nome lá dentro
# se quero checar se minha string tem o método upper , eu falaria :

if hasattr(string, 'upper'):
    print('Existe Upper aqui')
    print(string.upper())

print('\n\n')

"""
com o getattr eu posso passar um método para uma variavel

metodo = "upper"

e executar

"""

metodo_upper = 'upper'

if hasattr(string, metodo_upper):
    print('Existe este método')
    print(getattr(string, metodo_upper)())   
else:
    print('Não existe o metodo')
