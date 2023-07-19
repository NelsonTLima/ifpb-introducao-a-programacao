# -----------Atividade 04-------------------
# ------ Introdução à programação.----------

print(
        "1 - Escreva um programa, em Python, para ler 02(dois) números naturais (N∗).",
        "Calcular e exibir o maior valor entre os dois.\n",
        "casos de testes:\n",
        "_________________________",
        "|entrada:   |saída:     |",
        "|10         |20         |",
        "|20         |           |",
        "|___________|___________|",
        "|entrada:   |saída:     |",
        "|10         |10         |",
        "|10         |           |",
        "|___________|___________|\n\n",
        sep="\n"
        )

numero_um, numero_dois = int(input()), int(input())
if numero_um >= numero_dois:
    print(numero_um)
else:
    print(numero_dois)


#--------------------------------------------------------------
input("continue...")
print(
        "\n\n2 - Uma nota é considerada válida no sistema Suap se estiver entre 0 (zero) e 100(cem), inclusive.",
        "Escreva um programa para ler uma nota e informar se esta nota é válida para o Suap.\n",
        "casos de testes:\n",
        "_________________________",
        "|entrada:   |saída:     |",
        "|80         |Sim        |",
        "|___________|___________|",
        "|entrada:   |saída:     |",
        "|120        |Não        |",
        "|___________|___________|\n\n",
        sep="\n"
        )

nota = int(input())
if nota >= 0 and nota <= 100:
    print("Sim")
else:
    print("Não")


#------------------------------------------------------------------
input("continue...")
print(
        "\n\n3 - Escreva um programa para obter a data de nascimento (dia, mês e ano) de uma pessoa. Calcular e",
        "exibir a idade dessa pessoa. Considere a data 30/03/2023 como referência.\n"
        "casos de testes:\n",
        "_________________________",
        "|entrada:   |saída:     |",
        "|28         |23 anos    |",
        "|3          |           |",
        "|2000       |           |",
        "|___________|___________|",
        "|entrada:   |saída:     |",
        "|30         |23 anos    |",
        "|3          |           |",
        "|2000       |           |",
        "|___________|___________|",
        "|entrada:   |saída:     |",
        "|31         |22 anos    |",
        "|3          |           |",
        "|2000       |           |",
        "|___________|___________|\n\n",
        sep="\n"
        )

REFERENCIA_DIA, REFERENCIA_MES, REFERENCIA_ANO = 30, 3, 2023
dia, mes, ano = int(input()), int(input()), int(input())

idade = REFERENCIA_ANO - ano
if (REFERENCIA_MES <= mes) and (REFERENCIA_DIA < dia):
    idade = idade - 1
print(f"{idade} anos.")

#--------------------------------------------------------------
input("continue...")
print(
        "\n\n4- Escreva um programa para ler 03 (três) valores. Calcule e exiba se estes valores formam triângulo.\n",
        "formula:",
        "| b - c | < a < b + c = TRUE",
        "| a - c | < b < a + c = TRUE",
        "| a - b | < c < a + b = TRUE\n",
        "Exemplo:",
        "Com os três segmentos de reta medindo 5cm, 10cm e 9cm, podemos formar um triângulo?",
        "Vamos aplicar a regra da condição de existência de um triângulo para todos os lados.",
        "|10 – 9| < 5 < 10 + 9",
        "1 < 5 <19 (VERDADEIRO)\n",
        "|9 – 5| < 10 < 9 + 5",
        "4 < 10 < 14 (VERDADEIRO)",
        "|5 – 10| < 9 < 10 + 5",
        "5 < 9 < 15 (VERDADEIRO)\n\n",
        sep="\n"
        )

a, b, c = float(input()), float(input()), float(input())

if (abs(b - c) < a) and (a < (b + c)) and (abs(a - c) < b) and (b < (a + c)) and (abs(a - b) < c) and (c < (a + b)):
    print("VERDADEIRO")
else:
    print("FALSO")
