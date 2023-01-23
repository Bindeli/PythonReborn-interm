# Vamos falar mais sobre o modulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# a melhor estrutura de dados para eu salvar uma estrutura de dicionário no PYTHON é JSON
import json
# pessoa = {
#     'nome': 'Lucas',
#     'sobrenome': 'Bindeli',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.7,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# salvar isso em um arquivo

"""
A função json executa coisas simples

isso não inclui métodos, funções, classes, sets

objeto = dicionário > em json
Array = lista > em json

json é tudo number, não terá int ou float, mas o editor saberá qual é qual

true com t minúsculo

"""

"""
# a extensão informa pro editor que o arquivo tem json dentro dele
with open('aulajson.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa, 
        arquivo,
        indent=2 # para deixar os dados formatados
        )
    # json.dump(pessoa, arquivom,ensure_ascii=False) para fazer a pontução normalizar no arquivo
    # é bom deixar como estiver por conta de compartibilidade
    #dumps é para fazer dump em uma string
    #dum é para fazer dump em um arquivo

"""

# agora quero voltar os dados do arquivo para cá

with open('aulajson.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # load para carregar um arquivo
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])


# salvar só dados simples
# tupla é convertido para array/lista
# porém tupla é suportado