# URI [1002]
# Pegar as duas variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()
r = float(input())

pi = 3.14159

area = pi * pow(r, 2)

# formatar com 4 casas decimais
print("A={0:.4f}".format(area))
