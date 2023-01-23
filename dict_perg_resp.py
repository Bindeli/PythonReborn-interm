# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5','8'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51','16'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1','20'],
        'Resposta': '5',
    },
]
acertadas = 0
for questoes in perguntas:

    print('Pergunta: ', questoes['Pergunta'])

    opcoes = questoes['Opções']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice} : {opcao}')
    
    opcao_escolhida = input('\nDigite a opção de 0 a 4: ')

    escolha_int = None
    qtd_opcoes_pergunta = len(opcoes)

    if opcao_escolhida.isdigit():
        escolha_int = int(opcao_escolhida)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes_pergunta:
            if opcoes[escolha_int] == questoes['Resposta']:
                acertadas += 1
                print('Você acertou!\n')
            else:
                print('Você Errou!\n')




print(f'Total de questões acertadas : {acertadas}')
print('')