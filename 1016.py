# URI [1016]
# Pegar a variável
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

km = int(input())

# constantes
km_in_hour = 30
hour_in_minutes = 60

tempo_total = int((km * hour_in_minutes) / km_in_hour)

print("{tempo} minutos".format(tempo=tempo_total))