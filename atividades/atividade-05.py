from os import system
print("01. Escreva um programa, em python, para ler 10 números. Calcular e exibir a média dos números lidos.\n")

R = 10
soma = 0
for i in range(R):
    n = float(input("Digite um número: "))
    soma = soma + n
media = soma/R
print(f"A média entre esses {R} números será de: {media}.")

input()
system("clear")

print(
        "02. Escreva um programa, em Python, pra ler um número natural, calcular e exibir:\n",
        "Os números inteiros entre 1 e esse número lido, inclusive;",
        "Os divisores desse número;",
        "Se este número é primo;",
        "Se este número é perfeito ou não;",
        "Fatorial desse número;\n",
        sep="\n"
        )

n = int(input("Digite um número natural: "))

print("Os números inteiros entre 1 e esse número são: ", end="")
for i in range(1, n + 1):
    if i == n:
        print(f"{i}.")
    else:
        print(i, end=", ")

print("Os divisores desse número são: ", end="")
contador_de_divisores = 0
soma_dos_divisores = 0
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
    if n % i == 0:
        contador_de_divisores += 1
        soma_dos_divisores += i
        if i == n:
            print(f"{i}.")
        else:
            print(i, end=", ")

if contador_de_divisores <= 2:
    print("É PRIMO.")
else:
    print("NÃO É PRIMO.")

if soma_dos_divisores == n:
    print("É PERFEITO.")
else:
    print("NÃO É PERFEITO.")

print(f"O fatorial de {n} é: {fatorial}")


input()
system("clear")
print(
        "03. Esreva um programa, em Python, para ler 03 números (N, X ,Y). Calcule e exiba todos os números",
        "multiplos de N que estão entre X e Y.\n",
        sep="\n"
        )

n = int(input("Digite o numero N: "))
x = int(input("Digite o numero X: "))
y = int(input("Digite o numero Y: "))
if x > y:
    x , y = y , x

print("Os multiplos de N que estão entre X e Y são: ", end="")
checar_se_nenhum = None
for i in range(x,y + 1):
    if (i >= n) and (i % n == 0 or n % i == 0): 
        if checar_se_nenhum ==  None:
            print(i, end="")
        else:
            print(f", {i}", end="")
        checar_se_nenhum = i
if checar_se_nenhum == None:
    print(f"não existem multiplos de {n} entre {x} e {y}", end="")
print(".")

input()
system("clear")
print(
        "04. Escreva um programa, em Python, para ler as notas de 40 (quarenta) alunos. Com base na tabela,",
        "a seguir, informe a porcentagem de alunos aprovados e reprovados.\n",
        "______________________",
        "| nota     | Situação | ",
        "| 70 a 100 | Aprovado |",
        "| 40 a 69  | Final    |",
        "| 0 a 39   | Reprovado|",
        "|__________|__________|\n",
        sep="\n"
        )
R = 40
aprovados, final, reprovados = 0,0,0
for i in range(R):
    nota = int(input("Digite sua nota: "))
    if nota >= 70:
        aprovados += 1
    elif nota >= 40 and nota <= 69:
        final += 1
    else:
        reprovados += 1

porcentagem_aprovados = aprovados/R
porcentagem_final = final/R
porcentagem_reprovados = reprovados/R

print(
        f"Porcentagem de aprovados: {porcentagem_aprovados:.2%}",
        f"Porcentagem de estudantes na final: {porcentagem_final:.2%}",
        f"Porcentagem de reprovados: {porcentagem_reprovados:.2%}",
        sep="\n"
        )
