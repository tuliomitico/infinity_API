# Criado por Túlio em 30/11/2021
# language: pt
Funcionalidade: Login e Cadastro
  Cenario: Cadastro e Login
    Dado username="ana" senha="qwe" cpf="42246244005" telephone="3432107900" email="ana@mail.com"
    Quando logar com o usuario "ana" e senha "qwe"
    Entao sucesso
