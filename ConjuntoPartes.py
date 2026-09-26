
conjunto = [int(numero) for numero in input('Digite os elementos do conjunto: ').split()]

print('=' * 40)
print('       CONJUNTO DAS PARTES')
print('=' * 40)

print(f'Conjunto: {conjunto}')
print('=' * 40)

# Conjunto das partes
partes = [[]]

for elemento in conjunto:
    novas_partes = []

    for subconjunto in partes:
        novas_partes.append(subconjunto + [elemento])

    partes = partes + novas_partes

# Mostrando os subconjuntos
for subconjunto in partes:
    print(subconjunto)

print('=' * 40)

# Quantidade de subconjuntos
print('Quantidade de subconjuntos:', len(partes))

print('=' * 40)


