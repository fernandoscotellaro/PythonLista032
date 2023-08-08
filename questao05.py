'''
5)	Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo número.
'''

a = int(input("Insira aqui o primeiro número:"))
b = int(input("Insira aqui o segundo número:"))

soma = a + b
sub1 = a - b
sub2 = b - a
mut = a * b
div = a / b
rest = a % b

print("Esse é o valor da soma dos dois números:", (soma))
print("Esse é o valor da subtração do primeiro número pelo segundo:", (sub1))
print("Esse é o valor da subtração do segundo valor pelo primeiro:", (sub2))
print("Esse é o valor da multiplicação dos dois números:", (mut))
print("Esse é o valor da divisão do primeiro número pelo segundo:", (div))
print("Isso é o que restou da divisão dos números dados:", (rest))