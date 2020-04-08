# URI [1040]
# Pegar as variáveis
# Se utilizar python 2.x deve-se trocar o input() por raw_input()

n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print("Media: {med:.1f}".format(med=media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    n_exame = float(input())
    print("Nota do exame: {nota:.1f}".format(nota=n_exame))
    media = (media + n_exame) / 2
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {m_final:.1f}".format(m_final=media))