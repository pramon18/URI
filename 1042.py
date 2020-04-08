# URI [1042]
# Pegar as variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

a, b, c = map(int, input().split())

lista = [a, b, c]

# Ordenar
lista = sorted(lista)

print("{list_a}\n{list_b}\n{list_c}\n\n{a}\n{b}\n{c}"
      .format(list_a=lista[0], list_b=lista[1], list_c=lista[2], a=a, b=b, c=c))