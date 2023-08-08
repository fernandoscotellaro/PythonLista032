'''
6)	Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final do mês.
'''

nome = input("Insira aqui o seu nome completo:")
salario = int(input("Insira aqui o valor do seu salário fixo, sem a comissão de vendas: R$"))
vendas = int(input("insira aqui a quantidade de vendas que você efetuou:"))

acrescimo = vendas / 100
conta = (acrescimo * salario) + salario

print("Então", (nome), ", O valor do seu salário com o acréscimo de 15% de suas vendas é de: R$", (conta))