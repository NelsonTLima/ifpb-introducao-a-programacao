matriz = []

linha = int(input())
operacao = input()

for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    matriz.append(row)

soma = sum(matriz[linha])

if operacao == 'M':
    print(f"{soma/12:.1f}")
else:
    print(f"{soma:.1f}")
