from os import system

print(
        "1. Escreva um programa que leia 10 números inteiros e armazene-os em um vetor.",
        "imprima:\n",
        "- Os números que estão nos indices pares;",
        "- Os números que estão nos índices ímpares.\n",
        sep="\n"
        )

vetores = []
for i in range(10):
    n = int(input())
    vetores.append(n)

pares, impares = [], []
for i in range(len(vetores)):
    if i % 2 == 0:
        pares.append(vetores[i])
    else:
        impares.append(vetores[i])

print("Lista dos numeros nos indices pares: ", end="")
for i in range(len(pares)-2):
    print(f"{pares[i]}, ", end="")
print(f"{pares[len(pares)-1]}.")

print("Lista dos numeros nos indices impares: ", end="")
for i in range(len(impares)-2):
    print(f"{impares[i]}, ", end="")
print(f"{impares[len(impares)-1]}.")

input()
system("clear")
print(
        "2. Escreva um programa que leia um vetor V (contendo 20 inteiros) e um valor inteiro K,",
        "calcule e imprima a quantidade de ocorrencias de K dentro de V.\n",
        sep="\n"
        )

v = []
for i in range(20):
    v.append(input("Numero para v: "))
k = input("defina k: ")

print("qtd de ocorrencias:", v.count(k))

input()
system("clear")
print(
        "3. Escreva um programa que leia um vetor (contendo 20 inteiros) e um valor inteiro K,",
        "verifique e imprima se o K está ou não no vetor. Se estiver, informe em que posição (index).",
        "Obs.: K pode se repetir no vetor, neste caso mostre todas as posições onde o K aparece.\n",
        sep="\n"
        )

v = []
for i in range(20):
    v.append(input("Numero para v: "))
k = input("defina k: ")

if k in v:
    print("k está no vetor.")
    print("indice(s): ", end="")
    indexes = []
    for i in range(20):
        if v[i] == k:
            indexes.append(i)
    for i in range(0, len(indexes)):
        if i != len(indexes) - 1:
            print(f"{indexes[i]}, ", end="")
        else:
            print(f"{indexes[i]}.")
else:
    print("k não está no vetor.")

input()

system("clear")
print(
        "4. Escreva um programa que receba um vetor V de N numeros inteiros distintos (N será lido),",
        "determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices.\n",
        sep="\n"
        )

n = int(input("Defina n: "))
v = []
for i in range(n):
    v.append(int(input("digite um número: ")))
maior = max(v)
maior_indice = v.index(maior)
menor = min(v)
menor_indice = v.index(menor)

print("O maior:", maior)
print("Indice:", maior_indice)
print("O menor:", menor)
print("Indice:", menor_indice)
