import os, sys
def clear():
    if sys.platform == 'win32':
        os.system('cls') or None
    else:
        os.system('clear') or None

#------------------------------------//----------------------------------------//--------------------------

print("01. Escreva um programa para ler um número inteiro e informar se este número lido é par ou ímpar.\n")
n = int(input("Insira um número: "))
if n % 2 == 0:
    print("Número par.")
else:
    print("Número Impar.")

input("-->") ; clear()
print("\n02. Um professor realizou 03 (três) avaliações e ofereceu a turma a possibilidade de calcular a média de duas formas, podendo ser: aritmética ou ponderada (pesos: 4, 6 e 8). Escreva um programa para ler as 03(três) notas de um aluno e informar qual seria a melhor opção. Em caso de empate informe: tanto faz.\n")

n1, n2, n3 = float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: "))
p1, p2, p3 = 4, 6, 8

media_ponderada = (n1*p1 + n2*p2 + n3*p3)/(p1 + p2 + p3)
media_aritmetica = (n1 + n2 + n3)/3

if media_ponderada > media_aritmetica:
    print("media ponderada")
elif media_ponderada < media_aritmetica:
    print("media aritmetica")
else:
    print("Tanto faz.")

input("-->") ; clear()
print("\n03. Escreva um programa para ler o valor da renda mensal de um contribuinte, calcule e exiba qual é alíquota aplicada e o respectivo valor do imposto que deve ser pago.\n")

renda_mensal = float(input("Informe sua renda mensal: R$ "))

if renda_mensal < 1903.99:
    print("ISENTO")
elif renda_mensal >= 1093.99 and renda_mensal < 2836.66:
    aliquota = 0.075
    deducao = 142.8
    imposto = renda_mensal * aliquota - deducao
    print(f"A aliquota será de: {aliquota:.2%}")
    print(f"O imposto que deve ser pago será de R${imposto:.2f}")
elif renda_mensal >= 2836.66 and renda_mensal < 3751.07:
    aliquota = 0.15
    deducao = 354.8
    imposto = renda_mensal * aliquota - deducao
    print(f"A aliquota será de: {aliquota:.2%}")
    print(f"O imposto que deve ser pago será de R${imposto:.2f}")
elif renda_mensal >= 3751.07 and renda_mensal < 4664.69:
    aliquota = 0.225
    deducao = 636.13
    imposto = renda_mensal * aliquota - deducao
    print(f"A aliquota será de: {aliquota:.2%}")
    print(f"O imposto que deve ser pago será de R${imposto:.2f}")
else:
    aliquota = 0.275
    deducao = 869.36
    imposto = renda_mensal * aliquota - deducao
    print(f"A aliquota será de: {aliquota:.2%}")
    print(f"O imposto que deve ser pago será de R${imposto:.2f}")

input("-->") ; clear()
print("\n04. Um ano bissexto possui 366 dias, ou seja, um dia a mais do que os anos normais. Um ano é considerado bissexto quando uma das condições é satisfeita:\n - É múltiplo de 400;\n - É múltiplo de 4 e não é múltiplo de 100.\n\nEscreva um programa para ler um ano (número inteiro) e informar se este é um ano bissexto.\n")

ano = int(input("Informe o ano: "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("É BISSEXTO!")
else:
    print("NÃO É BISSEXTO.")
