from os import system

print(
        "01. Leia 5 valores inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados",
        "foram impares, quantos valores digitados foram positivos e quantos valores digitados foram negativos\n",
        "ENTRADA\n",
        "o arquivo de entrada contém 5 valores inteiros quaisquer.\n",
        "SAIDA\n",
        "Imprima a mensagem conforme o exemplo fornecido, uma margem por linha, não esquencendo o final de",
        "linha de cada uma.\n"
        " ______________________________________________",
        "| exemplo de entrada  | exemplo de saída       |",
        "|-5                   |3 valor(es) par(es)     |",
        "|0                    |2 valor(es) impar(es)   |",
        "|-3                   |1 valor(es) positivo(s) |",
        "|-4                   |3 valor(es) negativos(s)|",
        "|12                   |                        |",
        "|----------------------------------------------|\n",
        sep="\n"
        )

print("Digite 5 números:")
c_pares, c_impares, c_positivos, c_negativos = 0, 0, 0, 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        c_pares = c_pares + 1
    else:
        c_impares = c_impares + 1
    if n > 0:
        c_positivos = c_positivos + 1
    elif n < 0:
        c_negativos = c_negativos + 1

print(
        f"{c_pares} valor(es) par(es)",
        f"{c_impares} valor(es) impar(es)",
        f"{c_positivos} valor(es) positivo(s)",
        f"{c_negativos} valor(es) negativo(s)",
        sep="\n"
        )

input()
system("clear")
print(
        "02. Leia um valor inteiro X. Em seguida apresente os 6 valores impares consecutivos a partir de X, um valor por",
        "linha, inclusive X se for o caso.\n",
        "ENTRADA\n",
        "A entrada será um valor inteiro e positivo.\n",
        "SAIDA\n",
        "A saída será uma sequencia de seis números ímpares.\n",
        " ______________________________________________",
        "| exemplo de entrada  | exemplo de saída       |",
        "|8                    |9                       |",
        "|                     |11                      |",
        "|                     |13                      |",
        "|                     |15                      |",
        "|                     |17                      |",
        "|                     |19                      |",
        "|----------------------------------------------|\n",
        sep="\n"
        )

n = int(input("Digite um número: "))
for i in range(n, n+12):
    if i % 2 != 0:
        print(i)

input()
system("clear")
print(
        "03. Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de um até N, inclusive N, se for",
        "o caso.\n",
        "ENTRADA\n",
        "A entrada contém um valor inteiro de N (5<N<2000).\n",
        "SAÍDA\n",
        "Imprima o quadrado de cada um dos valores pares, de 1 a N, conforme o exemplo abaixo.\n",
        "Tome cuidado! Algumas linguagens tem por padrão apresentarem como saida 1e+006 ao invés de 1000000",
        "o que ocasionará resposta errada. Neste caso configure a precisão adequadamente para que isso não",
        "ocorra.\n",
        " ______________________________________________",
        "| exemplo de entrada  | exemplo de saída       |",
        "|6                    |2 ^ 2 = 4               |",
        "|                     |4 ^ 2 = 16              |",
        "|                     |6 ^ 2 = 36              |",
        "|----------------------------------------------|\n",
        sep="\n"
        )

n = int(input("Digite um número: "))
for i in range(1, n+1):
    if i % 2 == 0:
        quadrado = i**2
        print(f"{i} ^ 2 = {quadrado}")

input()
system("clear")
print(
        "04. Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.\n",
        "ENTRADA\n",
        "O arquivo de entrada coném 100 números, positivos e distintos.\n",
        "SAÍDA\n",
        "Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.\n"
        " ______________________________________________",
        "| exemplo de entrada  | exemplo de saída       |",
        "|2                    |3456                    |",
        "|113                  |4                       |",
        "|45                   |                        |",
        "|34565                |                        |",
        "|6                    |                        |",
        "|...                  |                        |",
        "|8                    |                        |",
        "|----------------------------------------------|\n",
        sep="\n"
        )

print("Digite 100 valores inteiros: ")
maior = None
for i in range(1,100):
    n = int(input(f"{i}º número:  "))
    if maior == None:
        maior = n
        posicao = i
    else:
        if n > maior:
            maior = n
            posicao = i
print(maior, posicao, sep="\n")


input()
system("clear")
print(
        "05. Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.\n",
        "ENTRADA\n",
        "Não há nenhuma entrada nesse problema.\n",
        "SAÍDA\n",
        "Imprima a sequencia conforme exemplo abaixo.",
        " ______________________________________________",
        "| exemplo de entrada  | exemplo de saída       |",
        "|                     |I=1 J=7                 |",
        "|                     |I=1 J=6                 |",
        "|                     |I=1 J=5                 |",
        "|                     |I=3 J=7                 |",
        "|                     |I=3 J=6                 |",
        "|                     |I=3 J=5                 |",
        "|                     |...                     |",
        "|                     |I=9 J=7                 |",
        "|                     |I=9 J=6                 |",
        "|                     |I=9 J=5                 |",
        "|----------------------------------------------|\n",
        sep="\n"
        )

input("Digite qualquer coisa para ver o resultado:\n\n")

for i in range(1,10,2):
    for j in range(7,4,-1):
        print(f"I={i} J={j}")
