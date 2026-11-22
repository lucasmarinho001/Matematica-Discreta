# ETAPA 2: HIPÓTESE DE INDUÇÃO
# A hipótese não se prova: nós SUPOMOS que a afirmação vale para um k qualquer
# programa só mostra o que estamos supondo, e confere para um k de exemplo

k = int(input("Escolha um valor de k para exemplo: "))

print()
print("HIPÓTESE DE INDUÇÃO:")
print(f"Suponha que 1 + 2 + ... + {k} = {k}({k}+1)/2")
print()

soma = 0
for i in range(1, k + 1):
    soma = soma + i

print("Para este k, a soma real é:", soma)
print("E a fórmula dá:            ", k * (k + 1) // 2)
print()
print("Na prova de verdade, k é qualquer número e apenas ASSUMIMOS que isso vale.")