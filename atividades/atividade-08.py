print("1. Escreva um programa que leia uma frase e a exiba “na vertical”, ou seja, com uma letra em cada linha.\n")

frase = input("Digite a frase: ")
for letra in frase:
    print(letra)

#----------------------------------------------
print("\n2. Escreva um programa que leia uma frase e determine a quantidade de brancos contidos na mesma.\n")

frase = input("Digite uma frase\n-> ")

c = 0
for i in frase:
    if i == " ":
        c += 1
print("Sua frase contém", c, "espaço(s) branco(s).")

#------------------------------------------------
print("\n3. Escreva um programa que leia uma frase e a exiba invertida.\n")

frase = list(input("Digite uma frase\n-> "))

for i in range((len(frase)//2)):
    frase[i], frase[len(frase) - i -1] = frase[len(frase) - i - 1], frase[i]

frase = ''.join(frase)
print(frase)

#-----------------------------------------------
print("\n4. Conjulgar verbos regulares.")

verbo = input("Digite um verbo: ")

match verbo[-2:]:
    case "ar":
        print(
                f"Eu {verbo[:-2]}o",
                f"Tu {verbo[:-2]}as",
                f"Ele {verbo[:-2]}a",
                f"Nós {verbo[:-2]}amos",
                f"Vós {verbo[:-2]}ais",
                f"Eles {verbo[:-2]}am",
                sep="\n"
                )
    case "er":
        print(
                f"Eu {verbo[:-2]}o",
                f"Tu {verbo[:-2]}es",
                f"Ele {verbo[:-2]}e",
                f"Nós {verbo[:-2]}emos",
                f"Vós {verbo[:-2]}eis",
                f"Eles {verbo[:-2]}em",
                sep="\n"
                )
    case "ir":
        print(
                f"Eu {verbo[:-2]}o",
                f"Tu {verbo[:-2]}es",
                f"Ele {verbo[:-2]}e",
                f"Nós {verbo[:-2]}imos",
                f"Vós {verbo[:-2]}is",
                f"Eles {verbo[:-2]}em",
                sep="\n"
                )
