# ETAPA 3: PASSO INDUTIVO
# Supondo que a soma até k é k(k+1)/2 (hipótese),
# mostramos que a soma até k+1 é (k+1)(k+2)/2.

k = int(input("Escolha um valor de k: "))

# Usamos a HIPÓTESE: a soma até k já é k(k+1)/2, sem somar tudo de novo.
soma_ate_k = k * (k + 1) // 2

# Somamos o próximo termo (k+1):
soma_ate_k_mais_1 = soma_ate_k + (k + 1)

# O que a fórmula diz para k+1:
formula_k_mais_1 = (k + 1) * (k + 2) // 2

print(f"Soma até k (pela hipótese):  {soma_ate_k}")
print(f"Somando o termo {k + 1}:           {soma_ate_k_mais_1}")
print(f"Fórmula aplicada em k+1:     {formula_k_mais_1}")

if soma_ate_k_mais_1 == formula_k_mais_1:
    print("O passo indutivo funcionou para este k! ✓")
else:
    print("O passo indutivo falhou! ✗")