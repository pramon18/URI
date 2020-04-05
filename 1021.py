# URI [1021]
# Pegar a variável
# Se utilizar python 2.x deve-se trocar o input() por raw_input()


def notas_ou_moedas(mo, fator):
    nc = int(mo / fator)
    mo = mo - (nc * fator)
    return nc, mo


valor = float(input())

# Pegar os centavos
centavos = int((valor - (int(valor))) * 100)

# Notas de 100
notas_de_cem, valor = notas_ou_moedas(valor, 100)

# Notas de 50
notas_de_cinquenta, valor = notas_ou_moedas(valor, 50)

# Notas de 20
notas_de_vinte, valor = notas_ou_moedas(valor, 20)

# Notas de 10
notas_de_dez, valor = notas_ou_moedas(valor, 10)

# Notas de 5
notas_de_cinco, valor = notas_ou_moedas(valor, 5)

# Notas de 2
notas_de_dois, valor = notas_ou_moedas(valor, 2)

# Moedas de 1 real
moedas_de_um = int(valor)

# Moedas de 50
moedas_de_cinquenta, centavos = notas_ou_moedas(centavos, 50)

# Moedas de 25
moedas_de_vintecinco, centavos = notas_ou_moedas(centavos, 25)

# Moedas de 10
moedas_de_dez, centavos = notas_ou_moedas(centavos, 10)

# Moedas de 5
moedas_de_cinco, centavos = notas_ou_moedas(centavos, 5)

# Moedas de 1 centavo
moedas_de_umcent = int(centavos)

print(str("NOTAS:\n" +
          "{cem} nota(s) de R$ 100.00\n" +
          "{cinq} nota(s) de R$ 50.00\n" +
          "{vint} nota(s) de R$ 20.00\n" +
          "{dez} nota(s) de R$ 10.00\n" +
          "{cinc} nota(s) de R$ 5.00\n" +
          "{dois} nota(s) de R$ 2.00\n" +
          "MOEDAS:\n" +
          "{um} moeda(s) de R$ 1.00\n" +
          "{mcinq} moeda(s) de R$ 0.50\n" +
          "{mvintc} moeda(s) de R$ 0.25\n" +
          "{mdez} moeda(s) de R$ 0.10\n" +
          "{mcinc} moeda(s) de R$ 0.05\n" +
          "{mum} moeda(s) de R$ 0.01").format(cem=notas_de_cem,
                                              cinq=notas_de_cinquenta,
                                              vint=notas_de_vinte,
                                              dez=notas_de_dez,
                                              cinc=notas_de_cinco,
                                              dois=notas_de_dois,
                                              um=moedas_de_um,
                                              mcinq=moedas_de_cinquenta,
                                              mvintc=moedas_de_vintecinco,
                                              mdez=moedas_de_dez,
                                              mcinc=moedas_de_cinco,
                                              mum=moedas_de_umcent))