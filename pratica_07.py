'''
print("Questão 1 \n")

v = [1, 2 ,3 , 4]
n = len(v)
print(v)

for i in range(n//2):
    j = n - i - 1
    v[i], v[j] = v[j], v[i]

print(v)

print("\n Questão dois.")

vetor_a = [0,2,4]
vetor_b = [1,3,6]

vetor_c = []

ca = cb = 0
for i in range(len(vetor_a)*2):
    if i % 2 == 0:
        vetor_c.append(vetor_a[ca])
        ca += 1
    else:
        vetor_c.append(vetor_b[cb])
        cb += 1
print(vetor_c)
print("3")
'''
lista = [1, 1, 2, 3 , 3, 4, 5, 6,6]
counts = []
moda = []

for i in lista:
    count = 0
    for j in lista:
        if j == i:
            count +=1
    counts.append(count)

for i in range(len(counts)):
    if counts[i] == max(counts):
        if lista[i] not in moda:
            moda.append(lista[i])

print("A moda é: ", end="")

for i in range(len(moda)):
    print(moda[i])

