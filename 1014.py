# URI [1014]
# Pegar as duas variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

distancia_total = float(input())
combustivel_gasto = float(input())

print("{0:.3f} km/l".format(distancia_total / combustivel_gasto))