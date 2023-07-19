# PRÁTICA DE INTRODUÇÃO Á PROGRAMAÇÃO.
#
#--------------------------------------------QUESTÃO 1---------------------------------------------------------

print("Questão 1:\n")
'''
O e-mail de qualquer pessoa é formado por duas partes: o login do usuário e o domínio do
provedor. Escreva um programa que leia o login de um usuário e o domínio do seu provedor e
mostre o seu e-mail completo:
Veja o exemplo abaixo.

Login: antonio.silva
Domínio: ifpb.edu.br
E-mail: antonio.silva@ifpb.edu.br
'''

# Resposta:

login = input("Login: ")
dominio = input("Domínio: ")
print(f"email: {login}@{dominio}")

#--------------------------------------------QUESTÃO 2---------------------------------------------------------

print("\nQuestão 2\n")
'''
O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Escreva um programa
para ler o peso do prato montado pelo cliente (em quilos) e exiba o valor a pagar. Assuma que a
balança já desconte o peso do prato.
'''

#reposta:

PRECO_KG = 25
peso = float(input("Informe o peso do prato: "))
print(f"Você deverá pagar: R$ {PRECO_KG * peso:.2f}")


#--------------------------------------------QUESTÃO 3---------------------------------------------------------

print("\nQuestão 3\n")
'''
A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$ 1.000,00
por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do valor da venda.
Escreva um programa para ler o nome, o número de carros vendidos e o valor total das vendas de
um vendedor, e calcule e exiba o seu salário final.
'''

# Resposta:

SALARIO = 1000
ADICIONAL_ABSOLUTO = 200
ADICIONAL_PERCENTUAL = 0.05

nome = input("Insira o nome do vendedor: ")
numero_de_vendas = int(input(f"Insira o número de carro vendidos por {nome}: "))
valor_total_vendas = float(input("insira o valor total das vendas: R$ "))

comissao = numero_de_vendas * ADICIONAL_ABSOLUTO + valor_total_vendas * ADICIONAL_PERCENTUAL
salario_final = SALARIO + comissao

print(f"Salário final: R$ {salario_final:.2f}")

#--------------------------------------------QUESTÃO 4---------------------------------------------------------

print("\nQuestão 4\n")
'''
Escreva um programa que efetue a apresentação do valor da conversão em real (R$) de um valor
lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e a quantidade de
dólares disponíveis com o usuário.
'''

# Reposta:

cotacao = float(input("Insira o valor da cotação do dolar: R$ "))
quantidade_de_dolares = float(input("Insira a quantidade de dolares: $ "))

conversao = quantidade_de_dolares * cotacao

print(f"A conversão será: R$ {conversao:.2f}")


#--------------------------------------------QUESTÃO 5---------------------------------------------------------

print("\nQuestão 5\n")
'''
Escreva um programa para ler as duas notas de um aluno. O programa deverá calcular e exibir a
média ponderada dessas duas notas. Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.
'''

# Resposta:

PESO_UM = 6
PESO_DOIS = 4

nota_um = float(input("Escreva o valor da primeira nota: "))
nota_dois = float(input("Escreva o valor da segunda nota: "))

media_ponderada = (nota_um * PESO_UM + nota_dois * PESO_DOIS)/(PESO_UM + PESO_DOIS)

print(f"A média ponderada será de: {media_ponderada}")

#--------------------------------------------QUESTÃO 6---------------------------------------------------------

print("\nQuestão 6\n")
'''
Escreva um programa para ler um tempo (hora, minuto e segundo), calcular e exibir esse tempo
em segundos.
Exemplo: 2 horas, 30 minutos e 50 segundos = 9050 segundos
'''

# Resposta:

PARA_A_MEDIDA_MENOR = 60

hora = int(input("hora: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))

total_de_minutos = hora * PARA_A_MEDIDA_MENOR + minutos
total_de_segundos = segundos + (total_de_minutos * PARA_A_MEDIDA_MENOR)

print(f"Valor total em segundos: {total_de_segundos} segundos.")
