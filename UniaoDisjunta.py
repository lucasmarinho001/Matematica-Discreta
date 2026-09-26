A = [int(numero) for numero in input('Digite os elementos do conjunto A: ').split()]
B = [int(numero) for numero in input('Digite os elementos do conjunto B: ').split()]

print('=' * 40)
print('         UNIÃO DISJUNTA')
print('=' * 40)

print(f'Conjunto A:, {A}')
print(f'Conjunto B:, {B}')

# Verificar se existem elementos em comum
disjuntos = True

for elemento in A:
    if elemento in B:
        disjuntos = False

# Resultado
print("-" * 40)

if disjuntos:
    print('Os conjuntos são disjuntos.')

    uniao = A + B

    print(f'União: {uniao}')

else:
    print('Os conjuntos NÃO são disjuntos.')

print('=' * 40)