from os import system

print(
        "1 - Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele",
        "no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,",
        "informar o total a receber no final do mês, com duas casas decimais.\n",
        "ENTRADA\n",
        "O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão",
        "(double) com duas casas decimais, representando o salário !xo do vendedor e montante total das vendas",
        "efetuadas por este vendedor, respectivamente.\n",
        "SAÍDA\n",
        "Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.\n",
        "___________________________________________",
        "| EXEMPLOS DE ENTRADA  | EXEMPLOS DE SAIDA |",
        "|                      |                   |",
        "|      JOAO            | TOTAL = R$ 684.54 |",
        "|      500.00          |                   |",
        "|      1230.30         |                   |",
        "|______________________|___________________|\n",
        sep="\n"
        )

vendedor = input("Informe o nome do vendedor: ")
salario = float(input("informe o salário do vendedor: R$ "))
total_de_vendas = float(input("Informe valor total das vendas: R$ "))
COMISSAO = 0.15

total = salario + (total_de_vendas * COMISSAO)

print(f"TOTAL = R$ {total:.2f}")

input()
system("clear")
print(
        "2 - Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um",
        "plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos",
        "cartesianos ou na origem (x = y = 0).",
        "Se o ponto estiver na origem, escreva a mensagem “Origem”.",
        "Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.\n",
        "ENTRADA\n",
        "A entrada contem as coordenadas de um ponto.\n",
        "SAÍDA\n",
        "A saída deve apresentar o quadrante em que o ponto se encontra.\n",
        "___________________________________________",
        "| EXEMPLOS DE ENTRADA  | EXEMPLOS DE SAIDA |",
        "|                      |                   |",
        "|4.5 -2.2              | Q4                |",
        "|0.1 0.1               | Q1                |",
        "|0.0 0.0               | Origem            |",
        "|______________________|___________________|\n",
        sep="\n"
        )

coordenadas = input("Insira as coordenadas: ")
coordenada_um, coordenada_dois = coordenadas.split()
coordenada_um, coordenada_dois = float(coordenada_um), float(coordenada_dois)

if coordenada_um > 0:
    if coordenada_dois > 0:
        quadrante = "Q1"
    elif coordenada_dois < 0:
        quadrante = "Q4"
    else:
        quadrante = "Eixo X"
elif coordenada_um < 0:
    if coordenada_dois > 0:
        quadrante = "Q2"
    elif coordenada_dois < 0:
        quadrante = "Q3"
    else:
        quadrante = "Eixo X"
else:
    if coordenada_dois == 0:
        quadrante = "Origem"
    else:
        quadrante = "Eixo Y"

print(quadrante)

input()
system("clear")
print(
        "3 - leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,",
        "uma linha em branco e em seguida, os valores na sequência como foram lidos.\n",
        "entrada\n",
        "a entrada contem três números inteiros.\n",
        "saída\n",
        "imprima a saída conforme foi especi!cado.\n",
        "___________________________________________",
        "| exemplos de entrada  | exemplos de saida |",
        "|                      |                   |",
        "|7 21 -14              | -14               |",
        "|                      |  7                |",
        "|                      |  21               |",
        "|                      |                   |",
        "|                      |  7                |",
        "|                      |  21               |",
        "|                      | -14               |",
        "|______________________|___________________|",
        "___________________________________________",
        "| exemplos de entrada  | exemplos de saida |",
        "|                      |                   |",
        "|-14 21 7              | -14               |",
        "|                      |  7                |",
        "|                      |  21               |",
        "|                      |                   |",
        "|                      | -14               |",
        "|                      |  21               |",
        "|                      |  7                |",
        "|______________________|___________________|\n",
        sep="\n"
        )

# Solução usando sort e listas. (Ainda não foi ensinado estruturas de repetição nem o método sort).
'''
valores = input("Digite três valores inteiros: ")
valor_um, valor_dois, valor_tres = valores.split()
lista_valores = [int(valor_um), int(valor_dois), int(valor_tres)]
lista_ordenada = sorted(lista_valores)
print(
        lista_ordenada[0],
        lista_ordenada[1],
        lista_ordenada[2],
        "",
        valor_um,
        valor_dois,
        valor_tres,
        sep="\n"
        )
'''
# Solução sem usar sort nem listas, nem estrutura de repetição.
valores = input("Digite três valores inteiros: ")
valor_um, valor_dois, valor_tres = valores.split()

a, b , c = int(valor_um), int(valor_dois), int(valor_tres)

if  a > c:
    a , c = c , a
if  a > b:
    a, b = b , a
if  b > c:
    b, c = c, b

print(
        a,
        b,
        c,
        "",
        valor_um,
        valor_dois,
        valor_tres,
        sep="\n"
        )

input()
system("clear")
print(
        "4 - Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem \"Sao Multiplos\" ou \"Nao ",
        "sao Multiplos\", indicando se os valores lidos são múltiplos entre si.\n",
        "entrada\n",
        "a entrada contem três números inteiros.\n",
        "saída\n",
        "imprima a saída conforme foi especi!cado.\n",
        "___________________________________________",
        "| exemplos de entrada  | exemplos de saida |",
        "|                      |                   |",
        "| 6 24                 | Sao multiplos     |",
        "| 6 25                 | Nao sao multiplos |",
        "|______________________|___________________|\n",
        sep="\n"
        )

valores = input("Digite dois valores: ")
valor_um, valor_dois = valores.split(" ")
valor_um, valor_dois = int(valor_um), int(valor_dois)

if valor_um <= valor_dois:
    resto = valor_dois % valor_um
else:
    resto = valor_um % valor_dois

if resto == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")
