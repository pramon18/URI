# URI [1020]
# Pegar a variável
# Se utilizar python 2.x deve-se trocar o input() por raw_input()


def idade_em_dias(dd, fator):
    am = int(dd / fator)
    dd = dd - (am * fator)
    return am, dd


dias = int(input())

# Anos
anos, dias = idade_em_dias(dias, 365)

# Minutos
meses, dias = idade_em_dias(dias, 30)

print("{aa} ano(s)\n{mm} mes(es)\n{dd} dia(s)".format(aa=anos, mm=meses, dd=dias))