"""
========================================================================
 PROGRAMA DE BOAS-VINDAS
========================================================================

DESCRIÇÃO 📋:
  Este script captura uma entrada do usuário (seu nome)
  e retorna uma mensagem de boas-vindas.

🎯 OBJETIVO:
    1. Ler o nome de uma pessoa fornecido.
    2. Armazenar o nome em uma variável.
    3. Exibir uma saudação personalizada usando o nome fornecido.
    4. Demonstrar o uso combinado das funções `input()` e `print()`.


🔍 O QUE FAZ:
    [1] Solicita a entrada do usuário:
      - A função `input()` exibe a pergunta 'Qual o seu nome? ' e aguarda
        que o usuário digite um texto e pressione Enter.

    [2] Armazena a informação:
      - O texto digitado pelo usuário é guardado na variável `nome`.

    [3] Exibe a mensagem formatada:
      - A função `print()` usa uma f-string (f'...') para construir a frase
        final, inserindo o conteúdo da variável `nome` na mensagem.


🧩 COMPONENTES UTILIZADOS:
    1. input()     (Função nativa para ler dados do teclado)
    2. print()     (Função nativa para exibir dados na tela)
    3. Variáveis   (Para armazenar o nome digitado)
    4. f-string    (Para formatação da mensagem de saída)
----------------------------------------------------------------------------------------------------
"""

# SCRIPT
nome = input('Qual o seu nome? ')
print(f'Olá, {nome}! É um prazer te conhecer.')