# INDUÇÃO COM DIVISIBILIDADE
# Afirmação: 7^n - 1 é divisível por 6, para todo n ≥ 1.
#
# Caso base: n = 1 -> 7 - 1 = 6, divisível por 6.
# Passo indutivo: se 7^k - 1 é divisível por 6, então
#   7^(k+1) - 1 = 7 * (7^k - 1) + 6
# e as duas parcelas são divisíveis por 6.

print("CASO BASE (n = 1):")
valor = 7 ** 1 - 1
print(f"  7^1 - 1 = {valor}, resto da divisão por 6: {valor % 6}")
print()

k = int(input("Escolha um k para o passo indutivo: "))

parte1 = 7 * (7 ** k - 1)   # divisível por 6 pela HIPÓTESE
parte2 = 6                  # divisível por 6 obviamente
total = parte1 + parte2

print()
print("PASSO INDUTIVO:")
print(f"  7^{k} - 1 = {7 ** k - 1}  (resto por 6: {(7 ** k - 1) % 6})")
print(f"  7 * (7^{k} - 1) = {parte1}  (resto por 6: {parte1 % 6})")
print(f"  parcela 6       = {parte2}  (resto por 6: {parte2 % 6})")
print(f"  Soma = {total}, e 7^{k + 1} - 1 = {7 ** (k + 1) - 1}")
print(f"  Resto de 7^{k + 1} - 1 por 6: {(7 ** (k + 1) - 1) % 6}")