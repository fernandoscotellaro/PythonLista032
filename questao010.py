'''
10)	Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

a = int(input("Qual o número total de eleitores do município?"))
b = int(input("Qual o número de votos brancos?"))
c = int(input("Qual o número de votos nulos?"))
d = int(input("Qual o número de votos válidos?"))

e = (b / a) * 100
f = (c / a) * 100
g = (d / a) * 100

print("")

print("O percentual de votos brancos é de", e, "%, de votos nulos é de", f, "% e o votos válidos é de", g, "%.")

