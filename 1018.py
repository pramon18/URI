# URI [1018]
# Pegar a variável
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

valor = int(input())

# Salvar valor inserido
entrada = valor

# Notas de 100
notas_de_cem = int(valor / 100)
valor = valor - int(notas_de_cem * 100)

# Notas de 50
notas_de_cinquenta = int(valor / 50)
valor = valor - int(notas_de_cinquenta * 50)

# Notas de 20
notas_de_vinte = int(valor / 20)
valor = valor - int(notas_de_vinte * 20)

# Notas de 10
notas_de_dez = int(valor / 10)
valor = valor - int(notas_de_dez * 10)

# Notas de 5
notas_de_cinco = int(valor / 5)
valor = valor - int(notas_de_cinco * 5)

# Notas de 2
notas_de_dois = int(valor / 2)
valor = valor - int(notas_de_dois * 2)

# Notas de 1
notas_de_um = valor

print(str("{valor}\n" +
          "{cem} nota(s) de R$ 100,00\n" +
          "{cinq} nota(s) de R$ 50,00\n" +
          "{vint} nota(s) de R$ 20,00\n" +
          "{dez} nota(s) de R$ 10,00\n" +
          "{cinc} nota(s) de R$ 5,00\n" +
          "{dois} nota(s) de R$ 2,00\n" +
          "{um} nota(s) de R$ 1,00").format(cem=notas_de_cem,
                                            cinq=notas_de_cinquenta,
                                            vint=notas_de_vinte,
                                            dez=notas_de_dez,
                                            cinc=notas_de_cinco,
                                            dois=notas_de_dois,
                                            um=notas_de_um,
                                            valor=entrada))