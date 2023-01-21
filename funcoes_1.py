"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.

Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.

Por padrão, funções Python retornam None (nada).
"""

def executar_print(frase):
    return print(f'Sua frase é esta: {frase}')


frase_escrita = 'Lucas Bindeli da Motta, the new dev'

executar_print(frase_escrita)

def saudacao(nome):
    print(f'Olá {nome}, tudo bem com você?!')

saudacao('Lucas Bindeli')