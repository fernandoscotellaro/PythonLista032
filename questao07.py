'''
7)	A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das prestações.
'''

valor = float(input("Insira aqui o valor do produto escolhido: R$"))
parcelas = int(input("Insira aqui a quantidade de parcelas que serão feitas:"))

conta = valor / parcelas

print("O valor de cada parcela sua será: R$", (conta))