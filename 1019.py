# URI [1019]
# Pegar a variável
# Se utilizar python 2.x deve-se trocar o input() por raw_input()


def hours_or_minutes(ss, fator):
    hm = int(ss / fator)
    ss = ss - (hm * fator)
    return hm, ss


segundos = int(input())

# Horas
horas, segundos = hours_or_minutes(segundos, 3600)

# Minutos
minutos, segundos = hours_or_minutes(segundos, 60)

'''
horas = int(segundos / 3600)
segundos = segundos - (horas * 3600)

minutos = int(segundos / 60)
segundos = segundos - (minutos * 60)
'''

print("{hh}:{mm}:{ss}".format(hh=horas, mm=minutos, ss=segundos))