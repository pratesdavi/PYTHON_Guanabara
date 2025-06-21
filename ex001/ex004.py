"""
========================================================================
 ANALISADOR DE STRINGS
========================================================================

DESCRIÇÃO 📋:
  Este script lê uma entrada do teclado, armazena em uma variável e
  realiza uma análise, exibindo o tipo primitivo do dado e outras
  informações obtidas através de métodos de verificação de strings.

🎯 OBJETIVO:
    1. Ler qualquer dado digitado pelo usuário.
    2. Exibir o tipo primitivo da variável (que `input` sempre retorna como `str`).
    3. Demonstrar o uso de diversos métodos de teste de strings (`is...()`).
    4. Apresentar um relatório detalhado sobre as características do texto
       fornecido.


🔍 O QUE FAZ:
    [1] Captura a entrada do usuário:
      - A função `input()` lê os dados do teclado e os armazena como uma
        string na variável `mensagem`.

    [2] Analisa e exibe o tipo da variável:
      - A função `type()` é usada para identificar a classe da variável.
      - O resultado é exibido na primeira linha da saída.

    [3] Executa uma série de testes booleanos:
      - O script invoca uma sequência de métodos de string (`.isspace()`,
        `.isnumeric()`, etc.) sobre a variável `mensagem`.
      - Cada metodo retorna um valor booleano (`True` ou `False`) que
        responde à pergunta feita.

    [4] Apresenta todos os resultados:
      - Cada um dos resultados booleanos é impresso na tela, precedido
        por uma descrição da verificação realizada.


🧩 COMPONENTES UTILIZADOS:
    1. input()              (Função para ler dados do teclado)
    2. print()              (Função para exibir dados na tela)
    3. type()               (Função para verificar o tipo de um objeto)
    4. Métodos de String:   (.isspace(), .isnumeric(), .isalpha(), .isalnum(),
                           .isupper(), .islower(), .istitle())
----------------------------------------------------------------------------------------------------
"""

# SCRIPT

valor = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúscula?', valor.isupper())
print('Está em minúscula?', valor.islower())
print('Está capitalizada?', valor.istitle())