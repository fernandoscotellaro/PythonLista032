'''
9)	Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

a = int(input("Insira aqui sua idade em anos:"))
b = int(input("Insira aqui sua idade em meses:"))
c = int(input("Insira aqui sua idade em dias:"))

d = (a * 365) + (b * 30) + (c)

print("O total de dias de vida é:", (d))