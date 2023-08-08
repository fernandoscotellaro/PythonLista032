'''
4)	Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula:  IMC = peso / altura2  -  Obs: peso em quilos e altura em metros.
'''

peso = int(input("Qual seu peso em quilogramas?"))
altura = float(input("Qual sua altura em metros?"))

altura2 = altura * altura
imc = peso / altura2

print("Seu índice de gordura corporal é:", (imc))