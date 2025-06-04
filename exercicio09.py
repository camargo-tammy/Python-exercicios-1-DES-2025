# Douglas está criando uma função simples no jogo que verifica se o número é múltiplo de 2 ou não (par ou ímpar).
# Escreva um programa que faça essa verificação.
numero = int(input("Digite seu número"))

if numero % 2 == 0:
    print(f"O número: {numero} é par, múltiplo de 2, parabéns!")
else:
    print(f"O número: {numero} é ímpar, portanto não é múltiplo de 2.")
