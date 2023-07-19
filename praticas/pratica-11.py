def menor(x, y, z):
    menor = None
    if x < y:
        menor = x
    else:
        menor = y
    if z < menor:
        menor = z
    return menor

teste_x = 3
teste_y = 1
teste_z = 7

teste = menor(teste_x, teste_y, teste_z)
if teste == teste_y:
    print("Passou no teste.")
else:
    print("Não passou no teste.")

#-------------------------------------

def print_e(string, n):
    nova_string = ""
    for i in string:
        nova_string += i + (n*" ")
    print(nova_string.strip())

#-----------------------------------

def soma(vetor):
    soma = 0
    for i in vetor:
        soma += i
    return soma

#----------------------------------

def fatorial(n):
    fator = 1
    for i in range(1, n+1):
        fator *= i
    return fator

if fatorial(5) == 120:
    print("Passou no teste.")
else:
    print("Não passou no teste.")
#---------------------------------

def calcular_media(x, y, z):
    return (x + y + z)/3

def retornar_conceito(media):
    if media >= 8:
        conceito = 'A'
    elif media >= 5:
        conceito = 'B'
    else:
        conceito = 'C'
    return conceito

nota_x, nota_y, nota_z = float(input()), float(input()), float(input())
media = calcular_media(nota_x, nota_y, nota_z)
conceito = retornar_conceito(media)

print("MEDIA: {:.1f}".format(media))
print("CONCEITO:", conceito)
