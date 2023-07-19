casos = []
maior = ''
while True:
    entrada = input().split()
    if entrada == ["0"]: break
    saida = ""
    for i in range(len(entrada)):
        if len(entrada[i]) > len(maior):
            maior = entrada[i]
        if i == len(entrada) - 1:
            saida += str(len(entrada[i]))
        else:
            saida += str(len(entrada[i]))
            saida += '-'
    casos.append(saida)

for i in casos:
    print(i)
print("\nThe biggest word:", maior)
