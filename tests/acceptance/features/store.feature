# Criado por Túlio em 02/12/2021
# language: pt
Funcionalidade: Ver lojas
  Cenario: Listar lojas
    Quando acessar "/store/"
    Entao retornar sucesso

  Cenario: Procurar loja 3
    Quando acessar a busca "/store/?search=l"
    Entao retornar outro sucesso
