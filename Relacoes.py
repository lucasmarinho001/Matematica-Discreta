# Conjunto de elementos
conjunto = [int(numero) for numero in input('Digite os elementos do conjunto: ').split()]

# Relação entre os elementos
quantidade = int(input('Quantos pares a relação terá? '))

relacao = []

for i in range(quantidade):
    a = int(input('Digite o primeiro elemento do par: '))
    b = int(input('Digite o segundo elemento do par: '))
    relacao.append((a, b))


print('=' * 45)
print('       ANALISADOR DE RELAÇÕES')
print('=' * 45)

print(f'Conjunto: {conjunto}')
print(f'Relação: {relacao}')

# Verificar se a relação é simétrica
simetrica = True

for a, b in relacao:
    if (b, a) not in relacao:
        simetrica = False

# Verificar se a relação é antissimetrica
antissimetrica = True

for a, b in relacao:
    if a != b and (b, a) in relacao:
        antissimetrica = False

# Mostrando os resultados
print('=' * 45)

print(f'Relação simétrica: {simetrica}')
print(f'Relação antissimétrica: {antissimetrica}')

print("=" * 45)