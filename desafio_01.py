print("Questão 1\n")

a, b, c, d = int(input()), int(input()), int(input()), int(input())
diferenca = a * b - c * d
print("DIFERENCA =", diferenca)

input()
print("Questão 2\n")

PI = 3.14159

a, b, c = input().split()
a,b,c = float(a), float(b), float(c)

triangulo = a*c/2
circulo = PI*(c**2)
trapezio = (a + b)*c/2
quadrado = b**2
retangulo = a * b

print(
        f"TRIANGULO: {triangulo:.3f}",
        f"CIRCULO: {circulo:.3f}",
        f"TRAPEZIO: {trapezio:.3f}",
        f"QUADRADO: {quadrado:.3f}",
        f"RETANGULO: {retangulo:.3f}",
        sep="\n"
        )

input()
print("Questão 3\n")

x1, y1 = input().split()
x2, y2 = input().split()
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"{distancia:.4f}")

input()
print("Questão 4")

value = int(input())
list_of_cedules = [100, 50, 20, 10, 5, 2, 1]

print(value)
for cedule in list_of_cedules:
    quantity = value // cedule
    value = value % cedule
    print(f"{quantity} nota(s) de R$ {cedule},00")
