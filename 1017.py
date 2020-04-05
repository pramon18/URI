# URI [1017]
# Pegar as duas variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

horas = int(input())
velocidade_media = int(input())

# constantes
km_por_litro = 12

combustivel = (velocidade_media * horas) / km_por_litro

print("{comb:.3f}".format(comb=combustivel))