# Questão 1

arquivo_1 = open(input(), "r")
arquivo_2 = open("COPIA.txt", "w")

texto = arquivo_1.read()
texto = texto.replace(" ", ".")

arquivo_2.write(texto)

arquivo_1.close()
arquivo_2.close()

# Questao 2

nome_arquivo, string = input().split()
with open(nome_arquivo, "a") as arquivo:
    arquivo.write(string)

# Questão 3

with open("teste", "r") as arquivo:
    n=1
    for linha in arquivo:
        print(n, linha, end="")
        n += 1

# Questão 4

texto = ""
for i in range(1,3):
    with open(input(f"Arquivo {i}: "), "r") as arquivo:
        texto += arquivo.read()

with open("concatenado", "a") as arquivo_resultante:
    arquivo_resultante.write(texto)

# Questão 5

cadastro = ""

n=0
while True:
    n+=1

    nome = input(f"Pessoa {n}\n\nNome: ")
    if nome == "": break
    sexo =  input("sexo: ").upper()
    idade = input("idade: ")

    print()

    pessoa = f"{nome},{sexo},{idade}\n"
    cadastro += pessoa

with open("CADASTRO.TXT", "w") as arquivo:
    arquivo.write(cadastro)

# Questão 6

homens = ""
mulheres = ""
with open("CADASTRO.TXT", "r") as cadastro:
    for linha in cadastro:
        nome, sexo, idade = linha.split(",")
        if sexo == 'M':
            homens += nome + "\n"
        else:
            mulheres += nome + "\n"

with open("homens.txt", "w") as arquivo:
    arquivo.write(homens)

with open("mulheres.txt", "w") as arquivo:
    arquivo.write(mulheres)
