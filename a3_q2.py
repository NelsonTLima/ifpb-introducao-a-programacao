#Escreva um programa para obter a descrição e o valor de um determinado produto.
#Considerando que será concedido um desconto de 20%, calcule e exiba:

# Descrição do produto;
# Desconto calculado;
# Valor final desse produto (com precisão de duas casas decimais após o ponto).

#--------------------------------//----------------------------------

descricao, preco = input("Descreva o produto:\n"), float(input("Informe o preço:\nR$ "))

desconto = preco * 0.2
valor_final = preco - desconto

print(
    "Descricao do produto:", str(descricao),
    "Valor do desconto:", "R$ " + str(desconto),
    "Valor final do produto:", "R$ " + str(valor_final),
    sep="\n"
)
