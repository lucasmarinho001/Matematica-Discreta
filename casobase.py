# ETAPA 1: CASO BASE
# Afirmação: 1 + 2 + ... + n = n(n+1)/2
# Aqui verificamos se ela vale para o primeiro valor (n = 1).

n = int(input("Valor do caso base (normalmente 1): "))

lado_esquerdo = 0
for i in range(1, n + 1):
    lado_esquerdo = lado_esquerdo + i

lado_direito = n * (n + 1) // 2

print("Lado esquerdo (soma de 1 até n):", lado_esquerdo)
print("Lado direito  (n(n+1)/2):       ", lado_direito)

if lado_esquerdo == lado_direito:
    print("O caso base vale! ✓")
else:
    print("O caso base NÃO vale! ✗")