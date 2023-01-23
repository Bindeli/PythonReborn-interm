#______________________________________________________________________________________________
# complexidade
def executa(funcao, *args): #funcao recebe soma, e args os parâmetros
    return funcao(*args)



def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda num: num*m,
    2
)

print(duplica(2))

print('\n')
print(
    executa( # primeiro passo os parâmetros, não temos retorno
        lambda x, y: x + y, 2, 3
    ),
    # executa(soma, 2,3) # mesma coisa que o lambda
    # soma(2,3)
)
#______________________________________________________________________________________________
# podemos passar args

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8,9
    )
)


#______________________________________________________________________________________________





#______________________________________________________________________________________________
