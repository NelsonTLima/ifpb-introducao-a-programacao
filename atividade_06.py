from os import system

print(
        "01. Escreva um programa para ler vários numeros. O programa deverá encerrar quando for informado",
        "o valor 0 (zero). Ao final, exiba o maior número informado.\n",
        sep="\n"
        )

n = int(input("Digite um número (ou 0 para encerrar): "))
maior = n
while (n != 0 ):
    n = int(input("Digite um número (ou 0 para encerrar): "))
    if (n > maior):
        maior = n
print("O maior é:", maior)

input()
system("clear")
print(
        "02. No sistema Suap uma not é considerada válida quando está no universo [0,100]. Escreva um",
        "programa para ler 01 (uma) nota válida no Suap. Ao final exibir",
        "   a. Nota válida;",
        "   b. Quantidade de valores inválidos que foram informados.\n",
        sep="\n"
        )

nota = int(input("Digite a nota: "))
qtd_invalidas = 0
while (nota > 100 or nota < 0):
    qtd_invalidas += 1
    nota = int(input("Digite a nota: "))
print(
        "Nota válida",
        f"A quantidade de notas inválidas foi de: {qtd_invalidas}",
        sep="\n"
        )

input()
system("clear")
print(
        "03. Escreva um programa para ler um número e informar se é par ou impar. Ao final, o programa",
        "deverá perguntar se o usuário deseja continuar (ou seja, digitar outro valor) ou sair. Se o usuário",
        "deseja continuar, o programa deverá repetir tudo novamente, caso contrário deverá encerrar.\n",
        sep="\n"
        )

while True:
    n = int(input("Digite um número inteiro: "))
    if (n%2 == 0):
        print("Número é par.\n")
    else:
        print("Número impar.\n")

    continua = input("Deseja continuar?\n(Digite 's' para continuar)\n")
    print()
    if (continua != 's'):
        break

input()
system("clear")
print(
        "04. Escreva um programa para ler vários números inteiros. O programa deverá encerrar quando for",
        "informado um valor negativo ou zero. Para cada número lido, o programa deverá exibir todos os",
        "divisores desse respectivo número. Ao final, o programa deverá exibir quantos números foram",
        "informados.\n",
        sep="\n"
        )

c = 0
n = int(input("informe um número: "))
while (n > 0):
    c += 1
    print(f"Os divisores de {n} são: ", end="")
    for i in range(1, n + 1):
        if (n % i == 0) and (i == n):
            print(f"{i}.\n")
        elif (n % i == 0) and (i < n):
            print(i, end=", ")

    n = int(input("informe um número: "))


print(f"\n{c} números foram informados.")
