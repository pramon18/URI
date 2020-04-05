# URI [1036]
# Pegar as variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

a, b, c = map(float, input().split())

# Bháskara
# x = (-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)

delta = pow(b, 2) - (4 * a * c)

if a != 0 and delta > 0:
    r1 = (-b + pow((pow(b, 2) - (4 * a * c)), (1/2))) / (2 * a)
    r2 = (-b - pow((pow(b, 2) - (4 * a * c)), (1/2))) / (2 * a)
    print("R1 = {0:.5f}\nR2 = {1:.5f}".format(r1, r2))
else:
    print("Impossivel calcular")

