# URI [1013]
# Pegar as três variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()


def maior(a, b):
    maior_a_b = ((a + b + abs(a - b)) / 2)
    return maior_a_b


a, b, c = map(int, input().split())

maior_todos = int(maior(a, b))
maior_todos = int(maior(maior_todos, c))

print("{0} eh o maior".format(maior_todos))