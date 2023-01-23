# -*- coding: windows-1252 -*-
# Criando arquivos com Python + Context Manager with
# Usamos a fun��o open para abrir
# um arquivo em Python (ele pode ou n�o existir)
# Modos:
# r (leitura), w (escrita), x (para cria��o)
# a (escreve ao final), b (bin�rio)
# t (modo texto), + (leitura e escrita)

# Context manager - with (abre e fecha)

# M�todos uteis
# write, read (escrever e ler)
# writelines (escrever v�rias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# Vamos falar mais sobre o modulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# Vamos falar mais sobre o modulo json, mas:
# json.dump = Gera um arquivo json
# json.load
#_____________________________________________________________________________________________
# caminho vou trabalhar com a pasta que estou

# no windows, toda vez que eu for colocar o caminho, que tem uma barra, vou colocar duas \\
# D:\\python_inter
# se n�o der certo, colocar o r'D:\\python_inter\\'
caminho_arquivo = 'D:\\python_inter\\'
caminho_arquivo += 'context.txt'

# modos de abertura - queremos abrir um arquivo, criando o arquivo
#_____________________________________________________________________________________________
# e como crio um arquivo ?

# open(caminho, modo) leitura, escrita, cria��oo, escreve ao final, bin�rio....
# se eu ir com r de cara, vai dar erro pois o arquivo não existe
# para criar, w, a , x

# arquivo = open(caminho_arquivo, 'w')
# # e sempre feche o arquivo
# arquivo.close()


# Context manager - algo que abre e fecha
# ele abre o arquivo e fecha pra mim
#_____________________________________________________________________________________________
"""
M�todos uteis : 

write - escreve e cria o arquivo
read - ler
+ - leitura e escrita

w ou a � os melhores - 
w - apaga tudo que est� nele e escreve o que eu mandar
a - escreve no final
"""
# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n') #no momento o cursor pr�prio do python esta na linha abaixo de linha 2
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0,0) # mover o cursor do python para o inicio do arquivo
    
#     print(arquivo.read()) # read move o cursor para baixo do arquivo
#     print('Lendo')
#     arquivo.seek(0,0)
#     print(arquivo.readline(), end='') # para corrigir e n�o ficar espa�o
#     print(arquivo.readline().strip()) # para remover o espa�o do come�o e final
#     arquivo.seek(0,0)
#     print('Readlines')
#     for linha in arquivo.readlines():
#         print(linha.strip())

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# w apaga tudo que est� no arquivo e escrever dnv
# with open(caminho_arquivo, 'w') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n') #no momento o cursor pr�prio do python est� na linha abaixo de linha 2
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#      )

# a eu escrevo no final
with open(caminho_arquivo, 'a', encoding='windows 1252') as arquivo:
    print(type(arquivo)) # o open retorna o text io wrapper
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n') #no momento o cursor próprio do python está na linha abaixo de linha 2
    arquivo.writelines(
        ('Aten��o!!')
        
     )
#_____________________________________________________________________________________________
# a partir do momento que eu come�o a colocar caracteres que podem gerar um transtorno
# vai aparecer bugado, como acento, � > no windows

"""
No canto inferior direito, aperte em UTF-8 , clica em reopen

pesquisei por windows 1252 (western) para tirar esse bug com caracteres especiais

se der erro, coloque isso no inicio do c�digo python

# -*- coding: windows-1252 -*-
"""
# enconding
#_____________________________________________________________________________________________
# Vamos falar mais sobre o modulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

import os

# excluir
# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)

os.rename(caminho_arquivo, 'context_2.txt')

#_____________________________________________________________________________________________

# Vamos falar mais sobre o modulo json, mas:
# json.dump = Gera um arquivo json
# json.load

