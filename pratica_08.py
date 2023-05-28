import random

print("Questão 1\n")

matriz_a = [
        [1, 2 ,3],
        [4, 5, 6]
        ]

matriz_b = [
        [1, 1, 1],
        [2, 2, 2]
        ]

matriz_c = [
        [0, 0, 0],
        [0, 0, 0]
        ]

for i in range(len(matriz_a[0])):
    for j in range(len(matriz_a)):
        matriz_c[j][i] = matriz_a[j][i] + matriz_b[j][i]

for i in matriz_c:
    print(i)


print("\nQuestão 2\n")

n = int(input("Digite o n da matriz: "))

matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(random.randint(0,9))

for i in matriz:
    print(i)

print()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i] == matriz[j]:
            print(matriz[i][j])

print()

print("\nQuestão 3\n")

matriz = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ]

matriz_b = []

for i in matriz:
    for j in range(len(i)):
        i[j] = random.randint(0,9)

for i in matriz:
    print(i)

for i in matriz[0]:
    matriz_b.append([])

for i in range(len(matriz[0])):
    for j in matriz:
        matriz_b[i].append(j[i])

print()

for i in matriz_b:
    print(i)
print()
