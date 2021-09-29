# infinity_API
API construída com finalidade de completar o desafio da Infinity Brasil

# Tecnologias

- [Django](https://www.djangoproject.com)
- [Swagger](https://swagger.io)
- [Django REST Framework](https://www.django-rest-framework.org)

# Rota do Swagger com a API em execução

[localhost:8000/docs/](https://localhost:8000/docs)

# Como executar a API

Para executar a API da Infinity, precisa instalar o Python e o Django e seus frameworks. A versão do Python utilizada é a 3.9.* e do Django 3.2.*.

## Baixar o Python

Baixe a versão através desse site [Python](https://www.python.org/downloads/), e escolha a versão 3.9

Clique no executavél e siga as instruções durante a instalação

## Git clone

Faça o clone desse repositório ou baixe o ZIP clicando no botão verde acima dos arquivos listados pelo GitHub, ou execute o seguinte comando no seu promp de comando favorito:

## `git clone https://github.com/tuliomitico/infinity_API.git`

## Acesse a pasta que foi clonado ou descompactado

Acesse a pasta e faça o seguinte comando:

## `pip install pipenv` ou `py -m venv venv`
##  `pipenv install -r requirements.txt` ou `cd venv/Scripts/activate && pip install -r requirements.txt`

Assim instalará todas as dependencias do projeto

## Fazendo as migrations

Para gera o SQLite é necessário realizar os seguintes comandos:

## `python manage.py makemigrations`
## `python manage.py migrate`

Com essas etapas concluídas poderá então executar a API com o seguinte comando:

## `python manage.py runserver`

Com isso ele irá subir a aplicação no localhost com a porta 8000.
