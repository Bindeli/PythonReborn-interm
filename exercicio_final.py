# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# comandos: listar, desfazer, refazer
# digite uma tarefa ou comando

import copy

def listar(tarefas):
    print('')
    if not tarefas:
        print('Você digitou nenhuma tarefa!')
        return
    print('Tarefas:')
    for elemento in tarefas:
        print(elemento)
    print('')

def desfazer(tarefas, tarefas_backup):
    print('')
    if not tarefas:
        print('Você digitou nenhuma tarefa!')
        return
    tarefa_apagada = tarefas.pop()
    print('Tarefa apagada com sucesso!')
    tarefas_backup.append(tarefa_apagada)

def refazer(tarefas, tarefas_backup):
    print('')
    if not tarefas:
        print('Não possui nada em tarefas')
        return
    tarefa_refazer = tarefas_backup.pop()
    print('Refeito com sucesso!')
    tarefas.append(tarefa_refazer)


lista_tarefas = []
tarefas_backup = []

while True:

    print('Comandos disponíveis: [1]Adicionar Tarefa [2]Listar [3]Desfazer [4]Refazer [4]Sair')
    opcao = input('Escolha sua opção: ')

    if not opcao.isdigit():
        print('Selecione uma opção disponível!')
        continue

    opcao = int(opcao)

    if opcao == 1:
        tarefa_atual = input('\nDigite sua tarefa a ser adicionada: ')
        lista_tarefas.append(tarefa_atual.strip())
        print(f'Tarefa "{tarefa_atual}" adicionada na lista de tarefas!!\n')
    elif opcao == 2: # Listar
        listar(lista_tarefas)
    elif opcao == 3: # Desfazer
        try:
            desfazer(lista_tarefas, tarefas_backup)
        except:
            print('Não há nada para desfazer!\n')
            continue
    elif opcao == 4: # Refazer
        try:
            refazer(lista_tarefas, tarefas_backup)
        except IndexError:
            print('Não há nada para refazer')
            continue
    elif opcao == 5: # Sair
        print('Finalizando!\n')
        break
    else:
        print('Digite uma opção válida!!\n')
    print('\n')