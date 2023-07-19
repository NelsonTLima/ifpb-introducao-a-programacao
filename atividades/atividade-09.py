frase = input()

for i in frase:
    frase = frase[1:] + frase[0]
    print(frase)
