n = int(input())
saidas = []
for i in range(n):
    texto = input().upper()
    chave = int(input())
    cifra = ""
    for caracter in texto:
        if caracter.isalpha():
            nova_posicao_ascii = ord(caracter) - chave
            if nova_posicao_ascii < 65:
                nova_posicao_ascii += 26
            novo_caracter = chr(nova_posicao_ascii)
        else:
            novo_caracter = caracter
        cifra += novo_caracter
    saidas.append(cifra)
for i in saidas:
    print(i)
