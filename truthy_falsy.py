# Valores Truthy e Falsy
"""
tipos mutáveis e imutáveis

Mutáveis [] {} set()
Imutáveis () "" 0 0.1 None False range(0,10)
"""
# todos os valores são falsos
lista = [] # if com lista vazia é false
dicionario = {} # if com dicionario vazio é falso também
conjunto = set() # falso
tupla = () # falso também
string = '' # é falso, ' ' string com um espaço já é considerada verdadeira
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

# se você fizer um if com eles, eles vão ser considerados falsos


def defina_falsy(valor):
    return 'falsy' if not valor else 'truthy'
    # se ele não tem valor, é falso, se não, é verdadeiro


print(f'TESTE', defina_falsy('TESTE'))
print(f'{lista}', defina_falsy(lista))
print(f'{dicionario}', defina_falsy(dicionario))
print(f'{conjunto}', defina_falsy(conjunto))
print(f'{tupla}', defina_falsy(tupla))
print(f'{string}', defina_falsy(string))
print(f'{inteiro}', defina_falsy(inteiro))
print(f'{flutuante}', defina_falsy(flutuante))
print(f'{nada}', defina_falsy(nada))
print(f'{falso}', defina_falsy(falso))
print(f'{intervalo}', defina_falsy(intervalo))

