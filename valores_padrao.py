"""
Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar : editar o seu código.

Toda vez que eu enviar um valor padrão, todos depois dele, também terá valor padrão

def soma(x, y , z=None, a=None):
    
"""
# is ou is not para saber se z não é None
def soma(x, y , z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
"""
Se tiver qualquer coisa que não seja None, ele irá usar o valor de Z

"""

soma(1,2) # x=1 y=2 3
soma(3,7,6) # x=3 y=7 z=6 16  






