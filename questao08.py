'''
8)	Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

a = int(input("Insira aqui o valor do produto: R$"))
b = int(input("insira aqui o valor que será acrescentado ao produto para venda, em porcentagem:"))

c = b / 100

print("Valor do produto com a porcentagem dada: R$", (a * c) + a)