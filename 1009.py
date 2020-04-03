# URI [1009]
# Pegar as três variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()
name = input()
fixed_salary = float(input())
sales = float(input())

final_salary = (fixed_salary + (sales * 0.15))

print("TOTAL = R$ {0:.2f}".format(final_salary))