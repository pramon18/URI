# URI [1012]
# Pegar as três variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

a, b, c = map(float, input().split())

pi = 3.14159

# (base * altura) / 2
triangulo = (a*c) / 2.0
# pi * R² (piralho ao quadrado)
circulo = pi * pow(c, 2)
# ((BaseMaior + BaseMenor) / 2) * h
trapezio = ((a + b) / 2.0) * c
# (Lado²)
quadrado = pow(b, 2)
# (LadoA * LadoB)
retangulo = (a * b)

print("TRIANGULO: {0:.3f}".format(triangulo))
print("CIRCULO: {0:.3f}".format(circulo))
print("TRAPEZIO: {0:.3f}".format(trapezio))
print("QUADRADO: {0:.3f}".format(quadrado))
print("RETANGULO: {0:.3f}".format(retangulo))
