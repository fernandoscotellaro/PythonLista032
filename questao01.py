'''
1)	Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o valor com o acréscimo dos 10% da gorjeta do garçom.
'''
conta = int(input("Insira aqui o valor de sua comanda do restaurante: R$"))
acrescimo = 0.10
print("Esse é o valor de sua conta com o acréscimo de 10% do garçom: R$", conta + (acrescimo * conta))