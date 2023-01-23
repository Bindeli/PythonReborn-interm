"""
Return - retorna determinado valor das funções


é a mesma coisa, pois print é uma função com o intuito de mostrar algo na tela
mostrar, ou seja, não tem valor, apenas de exibir
variavel = print('Lucas')
variavel = None

Se eu não colocar um return na função, ele irá rodar a função normalmente, mas irá retornar None

def soma(x, y)
    print(x + y)

soma1 = soma(2,2)
soma2 = soma(3,2)
print(soma1 + soma2) 

daria erro de typeerror, pois os dois valores possuem None como resultado, porém separados
iriam executar a função print da função e iria aparecer o valor.
Eu teria que colocar um return x+y, e aí sim iria gravar os valores nas variáveis
"""
print('')

def soma(x,y):
    return x + y
    print('Essa função não irá ocorrer')
    # tudo depois do return não irá executar

soma_1 = soma(10, 20)
soma_2 = soma(100,30)
print(f'Resultado : {soma_1} + {soma_2} = {soma_1 + soma_2}')
