# URI [1010]
# Pegar as três variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()
codigo_produto_1, quantidade_produto_1, preco_produto_1 = map(float, input().split())
codigo_produto_2, quantidade_produto_2, preco_produto_2 = map(float, input().split())

total_pagar = ((quantidade_produto_1 * preco_produto_1) + (quantidade_produto_2 * preco_produto_2))

print("VALOR A PAGAR: R$ {0:.2f}".format(total_pagar))