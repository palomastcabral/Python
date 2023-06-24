print("\n\n\t\tÂngulos côngruos")
angulo = int(input("\n -> Insira o valor do ângulo (em graus): "))

k = (angulo / 360)

if(angulo < 0):
    angulo = angulo * (-1)
    anguloInicial_negativo = True
else:
    anguloInicial_negativo = False

if(anguloInicial_negativo == False):
    mdp = (angulo % 360)
else:
    mdp = 360 - (angulo % 360)
    angulo = angulo * (-1)

print("\n | k = %d (2 voltas completas no sentido anti-horário)" %k)
print(" | Menor determinação positiva = %d°" %mdp)
print(" | %d° = %d° + (%d. 360°)" % (angulo, mdp, k))
print(" | %d° e %d° são arcos côngruos" % (angulo, mdp))
print(" | Expressão geral dos arcos côngruos = %d° + (k. 360°), sendo (k e Z)\n\n" %mdp)
