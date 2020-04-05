# URI [1035]
# Pegar a variável
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

a, b, c, d = map(int, input().split())

if (b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0) and (d > 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")