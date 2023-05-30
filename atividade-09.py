print("1. Faça um programa que leia uma frase e a exiba sem ps espaços em branco.\n")

frase = input("Digite a frase\n-> ").split()
print("".join(frase))

#-----------------------------------------------------------------------------------
print("\n2. Faça um programa que leia uma frase e a exiba com a inicial de cada palavra em maiúsculo.")

frase = input("Digite a frase\n-> ").split()

for i in range(len(frase)):
    palavra = list(frase[i])
    palavra[0] = palavra[0].upper()
    palavra = ''.join(palavra)
    frase[i] = palavra

for palavra in frase:
    print(palavra, end=' ')

#-----------------------------------------------------------------------------------
print("\n3. Faça um programa que leia uma frase (toda em letras maiúsculas) e a exiba criptografada. O método de criptografia será baseado na seguinte regra: trocar alguns caracteres por outros, conforme a tabela abaixo: A = ' ', E = 'U', I = 'O', O = 'i', U = 'E' " " = 'A' \n")

frase = input("Digite uma frase\n-> ").upper()

vetor_frase = []
for i in frase:
    vetor_frase.append(i)

for i in range(len(vetor_frase)):
    if vetor_frase[i] == 'A':
        vetor_frase[i] = ' '
    elif vetor_frase[i] == 'E':
        vetor_frase[i] = 'U'
    elif vetor_frase[i] == 'I':
        vetor_frase[i] = 'O'
    elif vetor_frase[i] == 'O':
        vetor_frase[i] = 'I'
    elif vetor_frase[i] == 'U':
        vetor_frase[i] = 'E'
    elif vetor_frase[i] == ' ':
        vetor_frase[i] = 'A'

for i in vetor_frase:
    print(i, end="")

#-----------------------------------------------------------------------------------
print("\n4. Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a string S com as suas vogais repetidas N vezes.")

VOGAIS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
frase = input("Digite uma frase\n-> ")
n = int(input("Digite o numero de vezes que as vogais irão repetir: "))

vetor_frase = []
for i in frase:
    vetor_frase.append(i)

for i in range(len(vetor_frase)):
    if vetor_frase[i] in VOGAIS:
        vetor_frase[i] = vetor_frase[i] * n
for i in vetor_frase:
    print(i, end='')
