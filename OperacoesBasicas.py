
# Entrada de Dados, e formatação dos valores para inteiro
conjunto_a = [int(x) for x in input('Digite o Conjunto A separadamente (ex: 1 2 3): ').split()]
conjunto_b = [int(x) for x in input('Digite o Conjunto B separadamente (ex: 3 4 5): ').split()]

# Armazenamentos dos resultados
uniao = []
intersecao = []
diferenca_a_b = []  
diferenca_b_a = []  

# União (A U B): Junção de todos elementos dos conjuntos
for elemento in conjunto_a:
    uniao.append(elemento)
for elemento in conjunto_b:
    if elemento not in uniao:
        uniao.append(elemento)

# Interseção (A n B): Junção apenas dos elementos que se repetem nos conjuntos
for elemento in conjunto_a:
    if elemento in conjunto_b:
        intersecao.append(elemento)

# Diferença (A - B): Tira do conjunto A o que tem em comum com o B
for elemento in conjunto_a:
    if elemento not in conjunto_b:
        diferenca_a_b.append(elemento)

# Diferença (B - A): Tira do conjunto B o que tem em comum com o A
for elemento in conjunto_b:
    if elemento not in conjunto_a:
        diferenca_b_a.append(elemento)

print('\n--- RESULTADOS ---')
print(f'Conjunto A:, {conjunto_a}')
print(f'Conjunto B:, {conjunto_b}')
print(f'União (A U B):, {uniao}')
print(f'Interseção (A n B): {intersecao}')
print(f'Diferença (A - B):, {diferenca_a_b}')
print(f'Diferença (B - A):, {diferenca_b_a}')