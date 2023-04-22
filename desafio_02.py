from os import system

print("Questão 1\n")

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = (b**2) - (4*a*c)

if a == 0 or delta <= 0:
    print("Impossivel calcular")
else:
    r1 = (-b + delta**0.5)/(2*a)
    r2 = (-b - delta**0.5)/(2*a)
    print(
            f"R1 = {r1:.5f}",
            f"R2 = {r2:.5f}",
            sep="\n"
            )

input()
system("clear")
print("Questão 2\n")

n = float(input())

if (n >= 0) and (n <= 25):
    print("Intervalo [0,25]")
elif (n > 25) and (n <= 50):
    print("Intervalo (25,50]")
elif (n > 50) and (n <= 75):
    print("Intervalo (50,75]")
elif (n > 75) and (n <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

input()
system("clear")
print("Questão 3\n")

h1, h2 = input().split()
h1, h2 = int(h1), int(h2)

if h1 < h2:
    t = h2 - h1
elif h1 > h2:
    t = h2 - h1 + 24
else:
    t = 24

print(f"O JOGO DUROU {t} HORA(S)")

input
system("clear")
print("Questão 4\n")

salary = float(input())

if (salary >= 0) and (salary <= 400):
    perc_raise = 0.15
elif (salary > 400) and (salary <= 800):
    perc_raise = 0.12
elif (salary > 800) and (salary <= 1200):
    perc_raise = 0.1
elif (salary > 1200) and (salary <= 2000):
    perc_raise = 0.07
else:
    perc_raise = 0.04

new_salary = salary * (1 + perc_raise)
salary_raise = salary * perc_raise
percent = int(perc_raise * 100)

print(
    f"Novo salario: {new_salary:.2f}",
    f"Reajuste ganho: {salary_raise:.2f}",
    f"Em percentual: {percent} %",
    sep="\n"
        )
