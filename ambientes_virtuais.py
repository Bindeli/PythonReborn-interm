# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.

# Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
# vou estar utilizando o python que está no ambiente virtual

# venv é o módulo que vamos usar para criar ambientes virtuais.

# Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:
# venv env .venv .env (. deixa oculto)

# é uma pasta e nessa pasta terá toda a instalação do python e tudo que estiver junto

# todas as bibliotecas de terceiros, irão para essa pasta

"""
Já que trabalhamos com várias empresas diferentes, teremos versões diferentes 

Como bibliotecas diferentes, e até versão de linguagem diferentes, antigos ou novos.

Não precisa enviar a pasta do venv para o repositório.
"""

"""
Ativando ...

python -m venv (nome do meu ambiente virtual)
venv 

terei a pasta include

lib - onde fica tudo que eu instalar de terceiros 

scripts - tem todos os executaveis que eu for utilizar no ambiente virtual

"""
"""
gcm python

para me mostrar o local que ele está

gcm python -Syntax - verificar só o caminho

"""

"""
Ativar o ambiente virtual muda o Path enquanto o sistema operacional estiver ativo
C:\Users\lucas\AppData\Local\Programs\Python\Python311\python.exe
D:\python_inter\venv\Scripts\python.exe

Acesso a pasta do ambiente virtual, vou em Scripts e abro o activate

ambiente\Scripts\activate

bin - para mac ou linux
. venv\bin\activate
source venv\bin\activate

deactivate - para desativar

"""

"""
ativando...
Para utilizar a versão do ambiente virtual, invés de utilizar e instalar pelo mensagem que recebemos

vá no canto inferior direito onde terá a versão do python 

Select interpreter
Python venv venv
"""

"""
pip index versions pymysql

ver as versões disponíveis
pip install pymysql=1.0.1

pip install pymysql --update 

vai instalar para a última versão
"""

"""
Gerar requirements.txt

código para jogar as versões para o requirements

pip freeze > requirements.txt 

(txt para visualizar as informações da versão )

se eu der pip install ...

no global, irá para todos os meus projetos !!!  atenção[!]

com o ambiente virtual posso ter uma versão diferente para cada ambiente
"""