"""
Argumentos nomeados e não nomeados em funções Python

Nomeados tem nome com sinal de igual
Argumento não nomeados recebe apenas o argumento (valor)

def soma(x,y)
    print(x+y)

soma(1,2) 

Argumento posicional, eu dependo da ordem para ele funcionar do jeito que eu quero


print(f'{x=} + y={y}')
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)
    # {x=} é a mesma coisa que y={y}

soma(1,2,3)
soma(7,3,4)

# para utilizar os argumentos eu puxo os parâmetros salvos na função e coloco nos argumentos
# quando puxo a função , igual o exemplo abaixo, assim a ordem não importa

soma(7, z=4, y=10)

# toda vez que eu nomeo um argumentos, o que vêm depois devo nomear também
# não poderia colocar assim : soma(7, z=4, 10) , daria erro
