from os import system

print(
        "01. Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para",
        "organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,",
        "quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.\n",
        "Este laboratório em especial utiliza tres tipos de cobaias: sapos, ratos e coelhos. Para obter estas",
        "informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia",
        "utilizada e a quantidade de cobaias utilizados em cada experimento.\n",
        "ENTRADA\n",
        "A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir.",
        "Cada caso de teste contém um inteiro Quantia (1 <= Quantia <= 15) que representa a quantidade de cobaias",
        "utilizadas e um caractere Tipo ('C','R', ou 'S'), indicando o tipo de cobaia (R: Rato S:Sapo C: Coelho).\n",
        "SAIDA\n",
        "Apresente o total de cobaias utilizadas, o total de cafa tipo de cobaia e o percentual de cada uma",
        "em relação ao total de cobaias utilizadas, sendo o percentual deve ser apresentado com dois digitos",
        "apos o ponto.\n"
        " __________________________________________________",
        "| exemplo de entrada  |     exemplo de saída       |",
        "|10                   |Total: 92 cobaias           |",
        "|10 C                 |Total de coelhos: 29        |",
        "|6 R                  |Total de ratos: 40          |",
        "|15 S                 |Total de sapos: 23          |",
        "|5 C                  |Percentual de coelhos 31.52%|",
        "|14 R                 |Percentual de ratos: 43.48% |",
        "|9 C                  |Percentual de sapos: 25.00% |",
        "|6 R                  |                            |",
        "|8 S                  |                            |",
        "|5 C                  |                            |",
        "|14 R                 |                            |",
        "|--------------------------------------------------|\n",
        sep="\n"
        )

r = int(input())
coelhos = ratos = sapos = total = 0
for i in range(r):
    experimento = input()
    n, cobaia = experimento.split()
    n = int(n)
    total = total + n
    if cobaia == 'C':
        coelhos = coelhos +  n
    elif cobaia == 'R':
        ratos = ratos +  n
    elif cobaia == 'S':
        sapos = sapos + n

perc_coelhos = coelhos/total * 100
perc_ratos = ratos/total * 100
perc_sapos = sapos/total * 100

print(
        f"Total: {total} cobaias",
        f"Total de coelhos: {coelhos}",
        f"Total de ratos: {ratos}",
        f"Total de sapos: {sapos}",
        f"Percentual de coelhos: {perc_coelhos:.2f} %",
        f"Percentual de ratos: {perc_ratos:.2f} %",
        f"Percentual de sapos: {perc_sapos:.2f} %",
        sep="\n"
        )

input()
system("clear")
print(
        "02. Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.\n",
        "ENTRADA\n",
        "Não há nenhuma entrada nesse problema.\n",
        "SAÍDA\n",
        "Imprima a sequencia conforme exemplo abaixo.\n",
        " ______________________________________________",
        "| exemplo de entrada  | exemplo de saída       |",
        "|                     |I=1 J=60                |",
        "|                     |I=4 J=55                |",
        "|                     |I=7 J=50                |",
        "|                     |...                     |",
        "|                     |I=? J=0                 |",
        "|----------------------------------------------|\n",
        sep="\n"
        )

input("Digite qualquer coisa para ver o resultado:\n\n")
i = 1
for j in range(60,-1,-5):
    print(f"I={i} J={j}")
    i = i+3
