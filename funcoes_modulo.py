"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
O que eu defino dentro da função, fica dentro do local que aquele código pode atingir

Existe o escopo global e local

O escopo global é o escopo onde todo o código é alcançavel

O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados

Não temos acesso a nomes de escopos internos nos escopos externos

A palavra global faz uma variavel do escopo externo ser a mesma no escopo interno
"""

def escopo_1():
    x = 1
    print(x)

# print(x) , não consigo acessar o x por aqui

escopo_1()

#___________________________________________________________________________________________________
# porém se eu declarar a variável de fora da função, eu consigo puxar para a função
print('')
z = 10

def escopo_z():
    print(z)

# z = 10
escopo_z()
# z = 10, se eu colocasse aqui, iria dar erro
#___________________________________________________________________________________________________

a = 20 # escopo global

def escopo_f():
    def outra_funcao():
        b = 5 # escopo interno
        # b é só desta função, mas essa função consegue acessar a e b
        print(a, b)
    outra_funcao()
    print(a)
    # print(b) não posso acessar o b da função
#___________________________________________________________________________________________________
"""
O escopo de dentro da função é protegido lá dentro
Tudo que eu defino dentro da função, eu não consigo alterar de fora da função
"""

valor_global = 10

def escopo_local():
    valor_global = 100

    print(valor_global)

print(valor_global) # 10
escopo_local()      # 100
print(valor_global) # 10


#___________________________________________________________________________________________________
"""
Para alterar o valor global de dentro da função, utilizamos o método global

global variavel

eu chamo ela dentro da função
"""

valor_a_ser_alterado = 10
print(f'\nAté aqui seu valor era: {valor_a_ser_alterado}')

def escopo_muda_global():
    global valor_a_ser_alterado
    valor_a_ser_alterado = 100
    print(f'Seu valor dentro da função é: {valor_a_ser_alterado}')

print(f'Seu valor antes de executar a função é: {valor_a_ser_alterado}')
escopo_muda_global()
print(f'Neste momento do valor é: {valor_a_ser_alterado}\n')

#___________________________________________________________________________________________________






#___________________________________________________________________________________________________