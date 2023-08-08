'''
3)	Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

peso = int(input("Qual o seu peso, em quilogramas?"))
altura = float(input("Qual sua altura em metros?"))

a = peso * 1000
b = altura * 100

print("Seu peso transferido de quilogramas para gramas é de:", (a))
print("Sua altura transferida de metros para centímetros é de:", (b), "cm")