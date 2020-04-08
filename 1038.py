# URI [1038]
# Pegar as variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

cod, qtd = map(int, input().split())

# Constantes
CACHORRO = 4.00
X_SALADA = 4.50
X_BACON = 5.00
TORRADA = 2.00
REFRI = 1.50

if cod == 1:
    print("Total: R$ {0:.2f}".format(qtd * CACHORRO))
elif cod == 2:
    print("Total: R$ {0:.2f}".format(qtd * X_SALADA))
elif cod == 3:
    print("Total: R$ {0:.2f}".format(qtd * X_BACON))
elif cod == 4:
    print("Total: R$ {0:.2f}".format(qtd * TORRADA))
elif cod == 5:
    print("Total: R$ {0:.2f}".format(qtd * REFRI))