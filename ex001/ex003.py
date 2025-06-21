"""
========================================================================
 PROGRAMA QUE REALIZA A SOMA DE DOIS NÚMEROS
========================================================================

DESCRIÇÃO 📋:
  Este script solicita que o usuário digite dois números inteiros, realiza a
  soma entre eles e exibe o resultado final.

🎯 OBJETIVO:
    1. Ler um primeiro número fornecido pelo usuário.
    2. Ler um segundo número fornecido pelo usuário.
    3. Converter a entrada (que é texto) para o tipo numérico inteiro.
    4. Realizar a operação de soma entre os dois números.
    5. Exibir uma mensagem descritiva com os números e o resultado da soma.


🔍 O QUE FAZ:
    [1] Lê e converte o primeiro número:
      - A função `input()` captura o primeiro valor como texto.
      - A função `int()` converte esse texto para um número inteiro, que é
        armazenado na variável `num1`.

    [2] Lê e converte o segundo número:
      - O mesmo processo é repetido para o segundo valor, que é guardado
        na variável `num2`.

    [3] Calcula a soma:
      - O operador de adição `+` é usado para somar os valores contidos
        em `num1` e `num2`. O resultado é armazenado na variável `soma`.

    [4] Exibe o resultado formatado:
      - A função `print()` usa uma f-string para mostrar a frase final,
        substituindo as variáveis pelos seus respectivos valores.


🧩 COMPONENTES UTILIZADOS:
    1. input()     (Função nativa para ler dados do teclado)
    2. int()       (Função de conversão para número inteiro)
    3. print()     (Função nativa para exibir dados na tela)
    4. Variáveis   (Para armazenar os valores e o resultado)
    5. Operador +  (Operador aritmético de adição)
    6. f-string    (Para formatação da mensagem de saída)
----------------------------------------------------------------------------------------------------
"""

# SCRIPT

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
soma = num1 + num2

print(f'A soma entre {num1} e {num2} é igual a {soma}!')