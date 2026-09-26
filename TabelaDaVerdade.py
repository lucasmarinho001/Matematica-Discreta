print('=' * 45)
print('           TABELA DA VERDADE')
print('=' * 45)

# Nomeação das colunas
print(' A      B       A AND B      A OR B      NOT A')
print('=' * 45)

valores = [True, False]

# Testa todas as combinações de A e B
for A in valores:
    for B in valores:

        # Resultado dos operadores lógicos
        print(f'{str(A):<6} {str(B):<8} {str(A and B):<12} {str(A or B):<11} {str(not A):<6}')

print('=' * 45)