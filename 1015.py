# URI [1015]
# Pegar as quatro variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()
from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Usando funcão da biblioteca math
distancia = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

# Usando função pow built-in
#distancia2 = pow((pow((x2 - x1), 2) + pow((y2 - y1), 2)), (1/2))

print("{0:.4f}".format(distancia))
#print("{0:.4f}".format(distancia2))