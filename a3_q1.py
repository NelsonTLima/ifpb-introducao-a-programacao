#Escreva um programa, em Python, para ler 02(dois) números naturais (N∗). Calcular e exibir:

# Soma dos dois números;
# Subtração do primeiro número pelo segundo;
# Multiplicação dos dois números;
# Divisão real do primeiro número pelo segundo;
# Divisão inteira do primeiro número pelo segundo;
# Resto da divisão do primeiro número pelo segundo;
# Potência do primeiro número pelo segundo.

#-----------------------------//--------------------

primeiro_numero, segundo_numero = int(input("Informe o primeiro número: ")), int(input("Informe o segundo número: "))

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero
resto = primeiro_numero % segundo_numero
potencia = primeiro_numero ** segundo_numero

print(
    "A soma dos dois números é:",soma, "\n",
    "A subtração do primeiro número pelo segundo é:", subtracao, "\n",
    "A multiplicação dos dois numeros é:", multiplicacao, "\n",
    "A divisão real do primeiro pelo segundo é:", divisao, "\n",
    "A divisâo inteira do primeiro pelo segundo é:", int(divisao), "\n",
    "O resto da divisão do inteiro pelo segundo é:", resto, "\n",
    "A potencia do primeiro número elevado ao segundo é:", potencia,
    sep=""
  )
