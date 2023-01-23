"""
args - Argumentos não nomeados

* - *args (empacotamento e desempacotamento)
"""

# Lembre-se de desempacotamento

# x, y, *resto = 1,2,4,5,6,7

# print(x,y, resto)

def soma(*args): # empacota o que eu enviar dentro de uma tupla
    total = 0
    for num in args:
        total += num
        print(num)
    return total

total_fun_soma = soma(1,2,3,4,5)
print(f'A soma da função foi : {total_fun_soma}')

print('\n\n')
#___________________________________________________________________________________________________
"""
Temos algo no Python que também faz isso, sum , que é soma

sum(valor_iterável)
"""
print('Utilizando a função sum:')
print(sum([1,2,3,4,5]))

#___________________________________________________________________________________________________
"""
Tomar cuidado com o desempacotamento
Por exemplo, no exemplo abaixo eu crio uma tupla
numeros = 1,2,3,4,5,6,7,8,9
outra_soma = soma(numeros)

e chamo a função com a tupla, vai dar erro, pois a função mesmo empacota
e com isso terei uma tupla dentro de uma outra tupla

como resolver?

Se eu tiver um iteravel e quiser passar para a função, eu devo desempacotar este valor
"""
print('\nDesempacotando jogando na função:')
numeros = 1,2,3,4,5,6,7,8,9
outra_soma = soma(*numeros)
print('Soma:',outra_soma, '\n')

print('\nAgora utilizando a função sum, eu não preciso desempacotar:')
print(f'Função sum com números: {sum(numeros)}')